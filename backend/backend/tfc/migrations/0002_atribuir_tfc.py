"""R7: atribuir um TFC numa só operação (docs/03_modelo_de_dados.md, secção 5.2; P-03.9 e P-03.10).

A função desencadeia as restantes operações: a proposta passa a Atribuída, o TFC é criado com os
seus alunos, a candidatura passa a Contemplada, as outras candidaturas dos alunos e as dos outros
candidatos a este TFC são encerradas, e as listas afetadas são renumeradas (trigger R8).
"""
from django.db import migrations

SQL = r"""
CREATE OR REPLACE FUNCTION atribuir_tfc(p_candidatura bigint, p_orientador bigint, p_coorientador bigint DEFAULT NULL)
RETURNS bigint LANGUAGE plpgsql AS $$
DECLARE
    c candidaturas_candidatura%ROWTYPE;
    v_prop propostas_proposta%ROWTYPE;
    v_alunos bigint[];
    v_tfc bigint;
BEGIN
    SELECT * INTO c FROM candidaturas_candidatura WHERE id = p_candidatura FOR UPDATE;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Candidatura % não existe.', p_candidatura;
    END IF;
    IF c.estado <> 'ATIVA' THEN
        RAISE EXCEPTION 'Só uma candidatura ativa pode ser contemplada (estado atual: %).', c.estado;
    END IF;
    SELECT * INTO v_prop FROM propostas_proposta WHERE id = c.proposta_id FOR UPDATE;
    IF v_prop.estado NOT IN ('DISPONIVEL', 'PRE_ATRIBUIDA') THEN
        RAISE EXCEPTION 'A proposta não pode ser atribuída (estado atual: %).', v_prop.estado;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM configuracao_docente WHERE id = p_orientador AND ativo) THEN
        RAISE EXCEPTION 'O orientador tem de ser um docente ativo.';
    END IF;

    IF c.grupo_id IS NULL THEN
        v_alunos := ARRAY[c.aluno_id];
    ELSE
        SELECT ARRAY[submissor_id, colega_id] INTO v_alunos FROM candidaturas_grupo WHERE id = c.grupo_id;
        UPDATE candidaturas_grupo SET estado = 'ATIVO' WHERE id = c.grupo_id;
    END IF;

    -- Proposta e TFC
    UPDATE propostas_proposta SET estado = 'ATRIBUIDA' WHERE id = v_prop.id;
    INSERT INTO tfc_tfc (proposta_id, ano_letivo_id, estado, orientador_id, coorientador_id,
                         repositorio_url, data_atribuicao, epoca_final)
    VALUES (v_prop.id, c.ano_letivo_id, 'EM_CURSO', p_orientador, p_coorientador, '', now(), 1)
    RETURNING id INTO v_tfc;
    INSERT INTO tfc_tfcaluno (tfc_id, aluno_id, ano_letivo_id, candidatura_id, ativo, data_entrada, motivo_saida)
    SELECT v_tfc, a, c.ano_letivo_id, CASE WHEN a = c.aluno_id THEN c.id END, true, current_date, ''
      FROM unnest(v_alunos) a;

    -- Candidaturas (cada mudança de estado dispara a renumeração das listas, R8)
    UPDATE candidaturas_candidatura SET estado = 'CONTEMPLADA', motivo_fim = '', data_estado = now()
     WHERE id = c.id;
    UPDATE candidaturas_candidatura SET estado = 'ENCERRADA', motivo_fim = 'ALUNO_CONTEMPLADO', data_estado = now()
     WHERE id <> c.id AND ano_letivo_id = c.ano_letivo_id
       AND estado IN ('PENDENTE_CONFIRMACAO', 'ATIVA')
       AND (aluno_id = ANY (v_alunos)
            OR grupo_id IN (SELECT id FROM candidaturas_grupo
                             WHERE submissor_id = ANY (v_alunos) OR colega_id = ANY (v_alunos)));
    UPDATE candidaturas_candidatura SET estado = 'ENCERRADA', motivo_fim = 'TFC_ATRIBUIDO_A_OUTRO', data_estado = now()
     WHERE proposta_id = v_prop.id AND id <> c.id
       AND estado IN ('PENDENTE_CONFIRMACAO', 'ATIVA');

    INSERT INTO comum_historico (entidade, entidade_id, evento, campo, valor_anterior, valor_novo, data, motivo)
    VALUES ('Proposta', v_prop.id, 'atribuir', 'estado', v_prop.estado, 'ATRIBUIDA', now(), '');

    RETURN v_tfc;
END $$;
"""

REVERSE = "DROP FUNCTION IF EXISTS atribuir_tfc(bigint, bigint, bigint);"


class Migration(migrations.Migration):
    dependencies = [
        ("tfc", "0001_initial"),
        ("candidaturas", "0003_regras_lista"),
        ("comum", "0002_initial"),
    ]
    operations = [migrations.RunSQL(SQL, REVERSE)]
