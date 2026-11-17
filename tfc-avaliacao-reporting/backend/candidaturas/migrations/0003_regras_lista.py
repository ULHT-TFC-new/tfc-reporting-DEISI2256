"""Regras da lista de candidaturas na base de dados (docs/03_modelo_de_dados.md, secção 5.2).

R8: quando uma candidatura sai da lista, as restantes são renumeradas de 1 a n, sem lacunas.
R9: validação de uma candidatura nova (fase, proposta, modalidade, limite e créditos).
P-03.4: função para mudar a prioridade de uma candidatura.
"""
from django.db import migrations

SQL = r"""
-- Lista de candidaturas: pendentes e ativas, do aluno (individuais) ou do grupo
CREATE OR REPLACE FUNCTION renumerar_lista(p_ano bigint, p_aluno bigint, p_grupo bigint)
RETURNS void LANGUAGE plpgsql AS $$
BEGIN
    -- 1.º passo: afastar as prioridades, para não violar o índice único durante a renumeração
    UPDATE candidaturas_candidatura SET prioridade = prioridade + 1000
     WHERE estado IN ('PENDENTE_CONFIRMACAO', 'ATIVA')
       AND CASE WHEN p_grupo IS NULL
                THEN grupo_id IS NULL AND aluno_id = p_aluno AND ano_letivo_id = p_ano
                ELSE grupo_id = p_grupo END;
    -- 2.º passo: numerar de 1 a n, mantendo a ordem
    UPDATE candidaturas_candidatura c SET prioridade = l.nova
      FROM (SELECT id, row_number() OVER (ORDER BY prioridade, id) AS nova
              FROM candidaturas_candidatura
             WHERE estado IN ('PENDENTE_CONFIRMACAO', 'ATIVA')
               AND CASE WHEN p_grupo IS NULL
                        THEN grupo_id IS NULL AND aluno_id = p_aluno AND ano_letivo_id = p_ano
                        ELSE grupo_id = p_grupo END) l
     WHERE c.id = l.id;
END $$;

-- R9: validar uma candidatura nova
CREATE OR REPLACE FUNCTION candidatura_validar_nova() RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE
    v_ano configuracao_anoletivo%ROWTYPE;
    v_prop propostas_proposta%ROWTYPE;
    v_colega bigint;
    v_n int;
BEGIN
    SELECT * INTO v_ano FROM configuracao_anoletivo WHERE id = NEW.ano_letivo_id;
    SELECT * INTO v_prop FROM propostas_proposta WHERE id = NEW.proposta_id;

    IF v_ano.estado <> 'ABERTO' THEN
        RAISE EXCEPTION 'O ano letivo % está fechado.', v_ano.designacao;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM configuracao_fase
                    WHERE ano_letivo_id = NEW.ano_letivo_id AND tipo = 'CANDIDATURAS'
                      AND now() BETWEEN data_inicio AND data_fim) THEN
        RAISE EXCEPTION 'A fase de candidaturas não está aberta.';
    END IF;
    IF v_prop.estado = 'PRE_ATRIBUIDA' THEN
        IF NOT EXISTS (SELECT 1 FROM propostas_propostaaluno
                        WHERE proposta_id = NEW.proposta_id AND aluno_id = NEW.aluno_id) THEN
            RAISE EXCEPTION 'Este TFC está pré-atribuído a outro aluno.';
        END IF;
    ELSIF v_prop.estado <> 'DISPONIVEL' THEN
        RAISE EXCEPTION 'Este TFC não está disponível para candidatura.';
    END IF;
    IF NEW.grupo_id IS NULL AND v_prop.modalidade = 'GRUPO' THEN
        RAISE EXCEPTION 'Este TFC é para grupos de 2 e não aceita candidaturas individuais.';
    END IF;
    IF NEW.grupo_id IS NOT NULL AND v_prop.modalidade = 'INDIVIDUAL' THEN
        RAISE EXCEPTION 'Este TFC é individual e não aceita grupos.';
    END IF;

    SELECT count(*) INTO v_n FROM candidaturas_candidatura
     WHERE estado IN ('PENDENTE_CONFIRMACAO', 'ATIVA')
       AND CASE WHEN NEW.grupo_id IS NULL
                THEN grupo_id IS NULL AND aluno_id = NEW.aluno_id AND ano_letivo_id = NEW.ano_letivo_id
                ELSE grupo_id = NEW.grupo_id END;
    IF v_n >= v_ano.max_candidaturas THEN
        RAISE EXCEPTION 'Atingiu o limite de % candidaturas. Retire uma candidatura de outro TFC.', v_ano.max_candidaturas;
    END IF;

    -- Créditos do aluno e, num grupo, também do colega
    IF NEW.grupo_id IS NOT NULL THEN
        SELECT CASE WHEN submissor_id = NEW.aluno_id THEN colega_id ELSE submissor_id END
          INTO v_colega FROM candidaturas_grupo WHERE id = NEW.grupo_id;
    END IF;
    IF EXISTS (SELECT a FROM unnest(ARRAY[NEW.aluno_id, v_colega]) a
                WHERE a IS NOT NULL
                  AND NOT EXISTS (SELECT 1 FROM configuracao_inscricaotfc i
                                   WHERE i.aluno_id = a AND i.ano_letivo_id = NEW.ano_letivo_id AND i.elegivel)) THEN
        NEW.estado := 'RECUSADA';
        NEW.motivo_fim := 'SEM_CREDITOS';
        NEW.prioridade := NULL;
        RETURN NEW;
    END IF;

    NEW.estado := CASE WHEN NEW.grupo_id IS NULL THEN 'ATIVA' ELSE 'PENDENTE_CONFIRMACAO' END;
    NEW.motivo_fim := '';
    NEW.prioridade := v_n + 1;  -- última posição da lista
    RETURN NEW;
END $$;

CREATE TRIGGER candidatura_validar_nova
BEFORE INSERT ON candidaturas_candidatura
FOR EACH ROW EXECUTE FUNCTION candidatura_validar_nova();

-- R8: a candidatura sai da lista → perde a prioridade e a lista é renumerada
CREATE OR REPLACE FUNCTION candidatura_antes_de_sair() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
    NEW.prioridade := NULL;
    RETURN NEW;
END $$;

CREATE OR REPLACE FUNCTION candidatura_depois_de_sair() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
    PERFORM renumerar_lista(NEW.ano_letivo_id, NEW.aluno_id, NEW.grupo_id);
    RETURN NULL;
END $$;

CREATE TRIGGER candidatura_antes_de_sair
BEFORE UPDATE OF estado ON candidaturas_candidatura
FOR EACH ROW
WHEN (OLD.estado IN ('PENDENTE_CONFIRMACAO', 'ATIVA') AND NEW.estado NOT IN ('PENDENTE_CONFIRMACAO', 'ATIVA'))
EXECUTE FUNCTION candidatura_antes_de_sair();

CREATE TRIGGER candidatura_depois_de_sair
AFTER UPDATE OF estado ON candidaturas_candidatura
FOR EACH ROW
WHEN (OLD.estado IN ('PENDENTE_CONFIRMACAO', 'ATIVA') AND NEW.estado NOT IN ('PENDENTE_CONFIRMACAO', 'ATIVA'))
EXECUTE FUNCTION candidatura_depois_de_sair();

-- R14 (parcial): histórico das mudanças de estado das candidaturas
CREATE OR REPLACE FUNCTION candidatura_historico() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO comum_historico (entidade, entidade_id, evento, campo, valor_anterior, valor_novo, data, motivo)
    VALUES ('Candidatura', NEW.id, 'mudança de estado', 'estado', OLD.estado, NEW.estado, now(), NEW.motivo_fim);
    RETURN NULL;
END $$;

CREATE TRIGGER candidatura_historico
AFTER UPDATE OF estado ON candidaturas_candidatura
FOR EACH ROW WHEN (OLD.estado IS DISTINCT FROM NEW.estado)
EXECUTE FUNCTION candidatura_historico();

-- P-03.4: mudar a prioridade de uma candidatura (as outras ajustam-se)
CREATE OR REPLACE FUNCTION mover_candidatura(p_id bigint, p_nova int)
RETURNS void LANGUAGE plpgsql AS $$
DECLARE
    c candidaturas_candidatura%ROWTYPE;
    v_n int;
BEGIN
    SELECT * INTO c FROM candidaturas_candidatura WHERE id = p_id FOR UPDATE;
    IF c.estado NOT IN ('PENDENTE_CONFIRMACAO', 'ATIVA') THEN
        RAISE EXCEPTION 'A candidatura não está na lista.';
    END IF;
    SELECT count(*) INTO v_n FROM candidaturas_candidatura
     WHERE estado IN ('PENDENTE_CONFIRMACAO', 'ATIVA')
       AND CASE WHEN c.grupo_id IS NULL
                THEN grupo_id IS NULL AND aluno_id = c.aluno_id AND ano_letivo_id = c.ano_letivo_id
                ELSE grupo_id = c.grupo_id END;
    p_nova := greatest(1, least(p_nova, v_n));
    IF p_nova = c.prioridade THEN RETURN; END IF;

    UPDATE candidaturas_candidatura SET prioridade = prioridade + 1000
     WHERE estado IN ('PENDENTE_CONFIRMACAO', 'ATIVA')
       AND CASE WHEN c.grupo_id IS NULL
                THEN grupo_id IS NULL AND aluno_id = c.aluno_id AND ano_letivo_id = c.ano_letivo_id
                ELSE grupo_id = c.grupo_id END;
    UPDATE candidaturas_candidatura SET prioridade = CASE
            WHEN id = p_id THEN p_nova
            WHEN prioridade - 1000 > c.prioridade AND prioridade - 1000 <= p_nova THEN prioridade - 1001
            WHEN prioridade - 1000 < c.prioridade AND prioridade - 1000 >= p_nova THEN prioridade - 999
            ELSE prioridade - 1000 END
     WHERE prioridade > 1000
       AND estado IN ('PENDENTE_CONFIRMACAO', 'ATIVA')
       AND CASE WHEN c.grupo_id IS NULL
                THEN grupo_id IS NULL AND aluno_id = c.aluno_id AND ano_letivo_id = c.ano_letivo_id
                ELSE grupo_id = c.grupo_id END;
END $$;
"""

REVERSE = r"""
DROP TRIGGER IF EXISTS candidatura_historico ON candidaturas_candidatura;
DROP TRIGGER IF EXISTS candidatura_depois_de_sair ON candidaturas_candidatura;
DROP TRIGGER IF EXISTS candidatura_antes_de_sair ON candidaturas_candidatura;
DROP TRIGGER IF EXISTS candidatura_validar_nova ON candidaturas_candidatura;
DROP FUNCTION IF EXISTS mover_candidatura(bigint, int);
DROP FUNCTION IF EXISTS candidatura_historico();
DROP FUNCTION IF EXISTS candidatura_depois_de_sair();
DROP FUNCTION IF EXISTS candidatura_antes_de_sair();
DROP FUNCTION IF EXISTS candidatura_validar_nova();
DROP FUNCTION IF EXISTS renumerar_lista(bigint, bigint, bigint);
"""


class Migration(migrations.Migration):
    dependencies = [
        ("candidaturas", "0002_initial"),
        ("configuracao", "0001_initial"),
        ("propostas", "0001_initial"),
        ("comum", "0002_initial"),
    ]
    operations = [migrations.RunSQL(SQL, REVERSE)]
