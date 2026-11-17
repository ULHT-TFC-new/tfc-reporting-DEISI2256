> **Aviso:** documento elaborado com apoio de IA generativa (Claude, Anthropic). A utilização, os prompts, as fontes e a revisão estão descritos em [04_utilizacao_de_ia.md](04_utilizacao_de_ia.md).

# 03 — Modelo de dados

Este documento descreve o modelo de dados da plataforma de gestão de TFC: as classes (que dão origem às tabelas da base de dados), os seus atributos e relações, as regras implementadas na própria base de dados e as vistas usadas no reporting. Parte dos processos descritos em [02_processos.md](02_processos.md).

## 1. Decisões de base

- **Base de dados:** PostgreSQL, feita de raiz e partilhada pelos três TFC (Reunião 4, 21/10).
- **Backend:** Python com Django (17/11). Cada classe deste documento corresponde a um modelo do Django e a uma tabela da base de dados. Os nomes das classes e dos atributos não têm acentos, porque passam diretamente para o código.
- **Lógica dos dados na base de dados:** as regras que garantem a consistência dos dados (estados, prioridades, prazos e cálculos) ficam em restrições, triggers e funções do PostgreSQL. Uma operação principal desencadeia as restantes, como na atribuição de um TFC (Reunião 4). A lógica de negócio que não é sobre dados (permissões, ficheiros, notificações e exportações) fica no backend (secção 7).
- **Histórico de todos os anos:** os dados estão sempre ligados a um ano letivo. Fechar o ano não apaga nada; os dados passam a ser só de leitura (P-01.4; Reunião 5, 28/10).
- **Ficheiros:** os relatórios e as imagens ficam numa pasta do servidor; a base de dados guarda só o caminho. Cada relatório enviado substitui o anterior (Reunião 7, 11/11).
- **Utilizadores:** usa-se o modelo de utilizador do Django, estendido com os dados de aluno, docente e entidade externa. Os perfis (aluno, docente, coordenação, administrador, organização de seminários e proponente externo) são grupos do Django, e um utilizador pode ter mais do que um.

## 2. Visão geral

O modelo está dividido em cinco áreas, pela ordem do ano letivo.

```mermaid
classDiagram
    direction LR
    class AnoLetivo
    class Utilizador
    class Aluno
    class Docente
    class Proposta
    class Candidatura
    class Grupo
    class TFC
    class TFCAluno
    class Entrega
    class ModeloAvaliacao
    class MomentoAvaliacao
    class Avaliacao
    class NotaMomento
    class ResultadoFinal

    AnoLetivo "1" -- "0..*" Proposta
    AnoLetivo "1" -- "0..*" ModeloAvaliacao
    Utilizador "1" -- "0..1" Aluno
    Utilizador "1" -- "0..1" Docente
    Proposta "1" -- "0..*" Candidatura
    Aluno "1" -- "0..*" Candidatura
    Grupo "0..1" -- "0..*" Candidatura
    Proposta "1" -- "0..1" TFC
    TFC "1" -- "1..2" TFCAluno
    Aluno "1" -- "0..*" TFCAluno
    Docente "1" -- "0..*" TFC : orienta
    ModeloAvaliacao "1" -- "1..*" MomentoAvaliacao
    TFC "1" -- "0..*" Entrega
    MomentoAvaliacao "1" -- "0..*" Entrega
    TFC "1" -- "0..*" Avaliacao
    Docente "1" -- "0..*" Avaliacao : jurado
    TFCAluno "1" -- "0..*" NotaMomento
    TFCAluno "1" -- "0..*" ResultadoFinal
```

| Área | Classes | Processos |
|---|---|---|
| 3.1 Configuração e utilizadores | AnoLetivo, Fase, Curso, GrupoCursos, UnidadeCurricular, Utilizador, Aluno, AlunoUC, InscricaoTFC, Docente, EntidadeExterna | MP-01 |
| 3.2 Propostas | Proposta, PropostaUC, Tecnologia, PropostaAluno, AnexoProposta | MP-02 |
| 3.3 Candidaturas e atribuição | Grupo, Candidatura, Selecao | MP-03 |
| 3.4 TFC, acompanhamento e entregas | TFC, TFCAluno, Pedido, Atividade, Entrega, VerificacaoAutomatica | MP-03, MP-04, MP-05 |
| 3.5 Avaliação e resultados | ModeloAvaliacao, MomentoAvaliacao, Criterio, MembroJuri, Defesa, Avaliacao, ClassificacaoCriterio, Seminario, Presenca, NotaMomento, ResultadoFinal | MP-06, MP-07, MP-08 |
| 3.6 Transversais | Notificacao, Historico | MP-09 e todos |

## 3. Classes por área

Em todas as tabelas, cada classe tem também um identificador `id` (chave primária), que não se repete nas listas de atributos. Os tipos indicados são os do PostgreSQL. As enumerações (estados e tipos) estão na secção 4.

### 3.1 Configuração e utilizadores (MP-01)

```mermaid
classDiagram
    class AnoLetivo {
        varchar designacao
        date data_referencia_elegibilidade
        int ects_minimos
        int min_candidaturas
        int max_candidaturas
        int max_orientacoes_sugeridas
        int antecedencia_relatorio_dias
        EstadoAnoLetivo estado
        timestamp data_fecho
    }
    class Fase {
        TipoFase tipo
        timestamp data_inicio
        timestamp data_fim
    }
    class Curso {
        varchar codigo
        varchar nome
        bool ativo
    }
    class GrupoCursos {
        varchar nome
        bool ativo
    }
    class UnidadeCurricular {
        varchar codigo
        varchar nome
    }
    class Utilizador {
        varchar email
        varchar nome
        bool ativo
    }
    class Aluno {
        varchar numero
    }
    class AlunoUC {
        EstadoUC estado
        numeric nota
    }
    class InscricaoTFC {
        int ects
        bool elegivel
    }
    class Docente {
        varchar departamento
        bool ativo
    }
    class EntidadeExterna {
        varchar nome
        TipoEntidade tipo
        varchar contacto
    }

    AnoLetivo "1" -- "1..*" Fase
    GrupoCursos "0..*" -- "1..*" Curso
    Utilizador "1" -- "0..1" Aluno
    Utilizador "1" -- "0..1" Docente
    Utilizador "0..*" -- "0..1" EntidadeExterna : representa
    Curso "1" -- "0..*" Aluno
    Aluno "1" -- "0..*" AlunoUC
    UnidadeCurricular "1" -- "0..*" AlunoUC
    Aluno "1" -- "0..*" InscricaoTFC
    AnoLetivo "1" -- "0..*" InscricaoTFC
```

| Classe | Atributos principais | Regras |
|---|---|---|
| AnoLetivo | designacao (ex.: "2026/27"), data de referência da elegibilidade, ECTS mínimos (90), mínimo e máximo de candidaturas (3 e 6), orientações sugeridas por docente (5), antecedência do relatório (7 dias), estado, data de fecho | Os valores do regulamento ficam como parâmetros do ano e podem mudar (P-01.1). Ano fechado → só leitura (P-01.4). |
| Fase | ano letivo, tipo, início e fim | As datas abrem e fecham as funcionalidades (P-01.1). Fim posterior ao início. |
| Curso | código (ex.: LEI), nome, ativo | Código único (P-01.3). |
| GrupoCursos | nome (ex.: "LEI + LIG"), ativo, cursos (N:M) | Desativar não apaga das propostas antigas (P-01.3). |
| UnidadeCurricular | código, nome | Usada no perfil do candidato e na seleção. |
| Utilizador | email, nome, ativo, perfis (grupos do Django), entidade externa | Email único. |
| Aluno | utilizador, número, curso | Número único. |
| AlunoUC | aluno, UC, estado (concluída ou em curso), nota | Usada no perfil do candidato e na ordenação da seleção (P-03.7). |
| InscricaoTFC | aluno, ano letivo, ECTS na data de referência, elegível | Um registo por aluno e ano. Elegível se ECTS ≥ mínimo do ano (cap. 4). |
| Docente | utilizador, departamento, ativo | Só os docentes ativos aparecem nas listas de escolha (P-01.2). |
| EntidadeExterna | nome, tipo (empresa ou departamento), contacto | O tipo define o formulário de proposta (P-02.1). |

### 3.2 Propostas (MP-02)

```mermaid
classDiagram
    class Proposta {
        varchar codigo
        varchar titulo
        text descricao
        varchar area_aplicacao
        Modalidade modalidade
        EstadoProposta estado
        TipoProponente tipo_proponente
        text notas_internas
        timestamp data_submissao
        timestamp data_publicacao
    }
    class PropostaUC {
        TipoLigacaoUC tipo
    }
    class Tecnologia {
        varchar nome
    }
    class PropostaAluno
    class AnexoProposta {
        varchar caminho_ficheiro
        varchar nome_original
    }

    AnoLetivo "1" -- "0..*" Proposta
    Utilizador "1" -- "0..*" Proposta : propõe
    EntidadeExterna "0..1" -- "0..*" Proposta
    Docente "0..1" -- "0..*" Proposta : orientador sugerido
    Proposta "0..1" -- "0..*" Proposta : continuação de
    Proposta "0..*" -- "1..*" Curso
    Proposta "1" -- "0..*" PropostaUC
    UnidadeCurricular "1" -- "0..*" PropostaUC
    Proposta "0..*" -- "0..*" Tecnologia
    Proposta "1" -- "0..2" PropostaAluno
    Aluno "1" -- "0..*" PropostaAluno
    Proposta "1" -- "0..*" AnexoProposta
```

| Classe | Atributos principais | Regras |
|---|---|---|
| Proposta | ano letivo, código, título, descrição, área de aplicação, modalidade, estado, tipo de proponente, proponente, entidade externa, orientador sugerido, coorientador sugerido, proposta de que é continuação, cursos (N:M), tecnologias (N:M), notas internas, datas | Estado inicial depende do proponente (P-02.1). Orientador sugerido tem de ser docente ativo. As notas internas só são visíveis para docentes e coordenação (pedido no inquérito). |
| PropostaUC | proposta, UC, tipo (requisito concluída, requisito em curso ou disciplina associada) | Define o perfil do candidato e as disciplinas associadas (P-02.1). |
| Tecnologia | nome | Tabela própria para permitir o filtro por tecnologia, o mais pedido no inquérito. |
| PropostaAluno | proposta, aluno | Aluno indicado ou pré-selecionado. No máximo 2 por proposta, e só 1 se a modalidade for individual. Um aluno não pode ser o 2.º elemento de duas propostas em grupo (P-02.1). |
| AnexoProposta | proposta, caminho do ficheiro, nome original | Anexos em PDF, pedidos pelos docentes no inquérito. |

### 3.3 Candidaturas e atribuição (MP-03)

```mermaid
classDiagram
    class Grupo {
        OrigemGrupo origem
        EstadoGrupo estado
        bool aceite_submissor
        bool aceite_colega
        timestamp data_criacao
    }
    class Candidatura {
        int prioridade
        EstadoCandidatura estado
        MotivoFim motivo_fim
        timestamp data_submissao
        timestamp data_estado
    }
    class Selecao {
        int posicao
        numeric pontuacao
        text justificacao_ajuste
        bool confirmada
    }

    AnoLetivo "1" -- "0..*" Grupo
    Aluno "1" -- "0..*" Grupo : submissor
    Aluno "1" -- "0..*" Grupo : colega
    Docente "0..1" -- "0..*" Grupo : propõe junção
    Proposta "1" -- "0..*" Candidatura
    Aluno "1" -- "0..*" Candidatura : submissor
    Grupo "0..1" -- "0..*" Candidatura
    Candidatura "0..1" -- "0..1" Candidatura : substitui
    Proposta "1" -- "0..*" Selecao
    Candidatura "1" -- "0..1" Selecao
```

| Classe | Atributos principais | Regras |
|---|---|---|
| Grupo | ano letivo, submissor, colega, origem (candidatura ou junção pelo docente), estado, docente que propôs a junção, aceitação de cada aluno, quem validou | Um aluno só pode estar num grupo ativo por ano (cap. 4). Na junção, os dois alunos aceitam e a coordenação valida (P-03.8). |
| Candidatura | ano letivo, proposta, aluno (submissor ou candidato individual), grupo (vazio se individual), prioridade, estado, motivo do fim, candidatura que substitui, datas | Ver as regras R1 a R6 da secção 5. A prioridade só existe enquanto a candidatura está na lista (pendente ou ativa). |
| Selecao | proposta, candidatura, posição, pontuação, justificação do ajuste, confirmada, quem confirmou | Guarda a ordenação e os ajustes da coordenação (P-03.7). |

### 3.4 TFC, acompanhamento e entregas (MP-03 a MP-05)

```mermaid
classDiagram
    class TFC {
        EstadoTFC estado
        varchar repositorio_url
        timestamp data_atribuicao
        int epoca_final
    }
    class TFCAluno {
        bool ativo
        date data_entrada
        date data_saida
        varchar motivo_saida
    }
    class Pedido {
        TipoPedido tipo
        text motivo
        text parecer_orientador
        EstadoPedido estado
        timestamp data_pedido
        timestamp data_decisao
    }
    class Atividade {
        TipoAtividade tipo
        date data
        text descricao
    }
    class Entrega {
        varchar relatorio_caminho
        timestamp relatorio_data_envio
        EstadoRelatorio estado_relatorio
        text comentario_orientador
        timestamp data_validacao
        varchar link_repositorio
        varchar commit_hash
        varchar link_video
        varchar link_versao_operacional
        text texto_divulgacao
        varchar imagem_caminho
        EstadoEntrega estado
        timestamp data_submissao
    }
    class VerificacaoAutomatica {
        ResultadoVerificacao resultado
        jsonb detalhes
        timestamp data
    }

    Proposta "1" -- "0..1" TFC
    Docente "1" -- "0..*" TFC : orientador
    Utilizador "0..1" -- "0..*" TFC : coorientador
    TFC "1" -- "1..2" TFCAluno
    Aluno "1" -- "0..*" TFCAluno
    Candidatura "0..1" -- "0..1" TFCAluno
    TFC "1" -- "0..*" Pedido
    TFC "1" -- "0..*" Atividade
    TFC "1" -- "0..*" Entrega
    MomentoAvaliacao "1" -- "0..*" Entrega
    Docente "0..1" -- "0..*" Entrega : valida relatório
    Aluno "0..1" -- "0..*" Entrega : submete
    Entrega "1" -- "0..*" VerificacaoAutomatica
```

| Classe | Atributos principais | Regras |
|---|---|---|
| TFC | proposta (1:1), ano letivo, estado, orientador, coorientador, repositório, data de atribuição, época da entrega final | Criado pela atribuição (R7). O orientador tem de ser docente ativo; aviso acima de 5 orientações (P-02.2). |
| TFCAluno | TFC, aluno, candidatura contemplada, ativo, datas de entrada e saída, motivo da saída | Liga 1 ou 2 alunos a um TFC e permite a dissociação de grupos e a desistência de um só elemento (P-04.2, P-03.12). Um aluno só tem um TFC ativo por ano (cap. 4). |
| Pedido | TFC, tipo (desistência, desatribuição, adiamento ou dissociação), aluno, quem pediu, motivo, parecer do orientador, estado, quem validou, datas | Junta numa só classe os pedidos que precisam de parecer e validação (P-03.12, P-03.13, P-04.2, P-04.3). |
| Atividade | TFC, autor, tipo (reunião ou atividade), data, descrição | P-04.1. |
| Entrega | TFC, momento, caminho do relatório, estado do relatório, comentário e validação do orientador, links (repositório, vídeo, versão operacional), hash do commit, texto de divulgação, imagem, quem submeteu, estado, datas | Uma entrega por TFC e momento. Só há um ficheiro de relatório: cada envio substitui o anterior (P-05.1). Bloqueada depois do prazo de entrega (R10). |
| VerificacaoAutomatica | entrega, resultado, detalhes (JSON), data | Resultado da verificação feita pelo DEISI2258. A forma de escrita ainda tem de ser combinada (questão 3 da secção 9). |

### 3.5 Avaliação e resultados (MP-06 a MP-08)

```mermaid
classDiagram
    class ModeloAvaliacao {
        int versao
        int niveis_escala
        int limiar_discrepancia
        numeric majoracao_orientador
        bool ativo
    }
    class MomentoAvaliacao {
        varchar nome
        TipoMomento tipo
        Mecanismo mecanismo
        bool com_nota
        numeric peso
        int epoca
        bool requer_entrega
        timestamp prazo_entrega
        timestamp prazo_avaliacao
        date data_publicacao
    }
    class Criterio {
        varchar nome
        text descricao
        numeric peso
        int ordem
    }
    class MembroJuri
    class Defesa {
        timestamp data_hora
        varchar local
    }
    class Avaliacao {
        EstadoAvaliacao estado
        text apreciacao
        timestamp data_submissao
        timestamp data_alteracao
    }
    class ClassificacaoCriterio {
        int nivel
        text justificacao_discrepancia
    }
    class Seminario {
        varchar titulo
        date data
    }
    class Presenca {
        bool presente
    }
    class NotaMomento {
        numeric valor
        OrigemNota origem
        EstadoNota estado
        timestamp data_publicacao
    }
    class ResultadoFinal {
        int epoca
        int nota_final
        Situacao situacao
        numeric percentagem_presencas
        EstadoNota estado
        timestamp data_publicacao
    }

    AnoLetivo "1" -- "1..*" ModeloAvaliacao
    ModeloAvaliacao "1" -- "1..*" MomentoAvaliacao
    MomentoAvaliacao "0..1" -- "0..*" MomentoAvaliacao : conta para
    MomentoAvaliacao "1" -- "0..*" Criterio
    TFC "1" -- "0..*" MembroJuri
    MomentoAvaliacao "1" -- "0..*" MembroJuri
    Docente "1" -- "0..*" MembroJuri
    TFC "1" -- "0..*" Defesa
    TFC "1" -- "0..*" Avaliacao
    MomentoAvaliacao "1" -- "0..*" Avaliacao
    Docente "1" -- "0..*" Avaliacao : jurado
    Avaliacao "1" -- "1..*" ClassificacaoCriterio
    Criterio "1" -- "0..*" ClassificacaoCriterio
    MomentoAvaliacao "1" -- "0..*" Seminario
    Seminario "1" -- "0..*" Presenca
    Aluno "1" -- "0..*" Presenca
    TFCAluno "1" -- "0..*" NotaMomento
    MomentoAvaliacao "1" -- "0..*" NotaMomento
    TFCAluno "1" -- "0..*" ResultadoFinal
```

| Classe | Atributos principais | Regras |
|---|---|---|
| ModeloAvaliacao | ano letivo, versão, níveis da escala (10), limiar de discrepância (2), majoração do orientador (0), ativo | Só um modelo ativo por ano. Alterar um modelo com avaliações cria uma nova versão (P-06.1). |
| MomentoAvaliacao | modelo, nome, tipo, mecanismo, com nota, peso, momento para que conta (vazio = nota final), época, requer entrega, prazos de entrega e de avaliação, data de publicação | O tipo corresponde aos modelos do modelo base: intercalar, final, DEISIFest e presenças, mais "outro" (P-06.1, P-06.3; Reunião 7). Soma dos pesos que contam para o mesmo destino = 100% (R12). |
| Criterio | momento, nome, descrição, peso, ordem | Soma dos pesos de um momento = 100% (P-06.2). |
| MembroJuri | TFC, momento, docente | O orientador não pode ser jurado nas avaliações intercalares (cap. 5). |
| Defesa | TFC, momento, data e hora, local | Publicada com pelo menos 48 h de antecedência (P-06.5). |
| Avaliacao | TFC, momento, jurado, estado (rascunho ou submetida), apreciação (texto com Markdown), datas | Uma avaliação por TFC, momento e jurado. O rascunho é guardado à medida que o jurado escreve, para o texto não se perder quando a sessão expira (pedido no inquérito). Bloqueada depois do prazo de avaliação (R10). |
| ClassificacaoCriterio | avaliação, critério, nível, justificação da discrepância | Nível entre 1 e o número de níveis da escala. Justificação obrigatória acima do limiar (R11). |
| Seminario | momento (do tipo presenças), título, data | Cada sessão de seminário de um momento de presença obrigatória. |
| Presenca | seminário, aluno, presente, quem registou | P-08.1. |
| NotaMomento | TFC e aluno, momento, valor (2 casas decimais), origem (calculada, votação ou manual), estado (calculada, confirmada ou publicada), data de publicação | Uma nota por aluno e momento. O resultado do DEISIFest entra aqui com origem "votação" (P-08.2). |
| ResultadoFinal | TFC e aluno, época, nota final (inteiro), situação, percentagem de presenças, estado, data de publicação | P-07.2 e P-07.3. Aprovado com nota ≥ 10 e presenças ≥ 70% (cap. 5 e 6). |

### 3.6 Transversais

| Classe | Atributos principais | Regras |
|---|---|---|
| Notificacao | destinatário, tipo, mensagem, ligação, lida, email enviado, data | Base do subsistema de notificações (P-09.4), a detalhar na arquitetura. |
| Historico | entidade, identificador do registo, evento, campo, valor anterior, valor novo, utilizador, data, motivo | Preenchido por triggers sempre que muda um estado, uma prioridade, uma nota ou um dado já publicado (R14). Dá o histórico pedido em vários processos e a auditoria das correções. |

## 4. Enumerações

Os estados seguem as máquinas de estados da secção 4 de [02_processos.md](02_processos.md).

| Enumeração | Valores |
|---|---|
| EstadoAnoLetivo | ABERTO, FECHADO |
| TipoFase | PROPOSTAS_DOCENTES, PROPOSTAS_EXTERNAS, PROPOSTAS_ALUNOS, VALIDACAO_PROPOSTAS_ALUNOS, CANDIDATURAS, LISTA_FINAL |
| EstadoUC | CONCLUIDA, EM_CURSO |
| TipoEntidade | EMPRESA, DEPARTAMENTO |
| Modalidade | INDIVIDUAL, GRUPO, INDIVIDUAL_OU_GRUPO |
| TipoProponente | DOCENTE, ALUNO, EMPRESA, DEPARTAMENTO |
| EstadoProposta | EM_VALIDACAO, ALTERACOES_SOLICITADAS, ACEITE, RECUSADA, DISPONIVEL, PRE_ATRIBUIDA, ATRIBUIDA, ARQUIVADA |
| TipoLigacaoUC | REQUISITO_CONCLUIDA, REQUISITO_EM_CURSO, ASSOCIADA |
| OrigemGrupo | CANDIDATURA, JUNCAO |
| EstadoGrupo | PENDENTE, ATIVO, RECUSADO, DISSOLVIDO |
| EstadoCandidatura | PENDENTE_CONFIRMACAO, ATIVA, RECUSADA, CONTEMPLADA, ENCERRADA, CANCELADA |
| MotivoFim | SEM_CREDITOS, TFC_ATRIBUIDO_A_OUTRO, ALUNO_CONTEMPLADO, RECUSADA_PELO_COLEGA, SEM_CONFIRMACAO, DESISTENCIA, CANCELADA_PELO_ALUNO, SUBSTITUIDA |
| EstadoTFC | EM_CURSO, ADIADO, ENTREGUE, AVALIADO, CONCLUIDO, CANCELADO, ARQUIVADO |
| TipoPedido | DESISTENCIA, DESATRIBUICAO, ADIAMENTO, DISSOCIACAO |
| EstadoPedido | PENDENTE, VALIDADO, REJEITADO |
| TipoAtividade | REUNIAO, ATIVIDADE |
| EstadoRelatorio | ENVIADO, ACEITE, DEVOLVIDO |
| EstadoEntrega | POR_SUBMETER, SUBMETIDA, EM_FALTA |
| ResultadoVerificacao | CUMPRE, NAO_CUMPRE, ERRO |
| TipoMomento | INTERCALAR, FINAL, DEISIFEST, PRESENCAS, OUTRO |
| Mecanismo | JURI_CRITERIOS, VOTACAO, PRESENCA |
| EstadoAvaliacao | RASCUNHO, SUBMETIDA |
| OrigemNota | CALCULADA, VOTACAO, MANUAL |
| EstadoNota | CALCULADA, CONFIRMADA, PUBLICADA |
| Situacao | APROVADO, REPROVADO, EXCLUIDO |

## 5. Regras na base de dados

A base de dados garante estas regras, mesmo que o pedido não venha do backend (por exemplo, quando o DEISI2258 escreve diretamente na base de dados).

### 5.1 Restrições

| # | Regra | Implementação | Processo |
|---|---|---|---|
| R1 | Um aluno não se candidata duas vezes ao mesmo TFC | Índice único parcial em Candidatura (proposta, aluno) para os estados pendente e ativa | P-03.1, P-03.2 |
| R2 | A lista de candidaturas não tem prioridades repetidas | Índice único parcial em Candidatura (aluno ou grupo, prioridade) para os estados pendente e ativa | P-03.4 |
| R3 | Um aluno só tem um TFC ativo por ano | Índice único parcial em TFCAluno (aluno, ano letivo) quando ativo | P-03.9 |
| R4 | Um aluno só está num grupo ativo por ano | Índice único parcial em Grupo, para o submissor e para o colega | P-03.2, P-03.8 |
| R5 | Níveis, pesos e notas dentro dos limites | Restrições CHECK (por exemplo, nível entre 1 e 10, peso entre 0 e 100, nota entre 0 e 20) | P-06.1, P-06.6 |
| R6 | Uma entrega por TFC e momento; uma avaliação por TFC, momento e jurado | Restrições UNIQUE | P-05.3, P-06.6 |

### 5.2 Triggers e funções

| # | Regra | Implementação | Processo |
|---|---|---|---|
| R7 | **Atribuir um TFC** desencadeia as restantes operações: a proposta passa a Atribuída, o TFC é criado no estado Em curso com os seus alunos, a candidatura passa a Contemplada, as outras candidaturas do aluno são encerradas e as candidaturas dos outros alunos a esse TFC também (R8) | Função `atribuir_tfc(candidatura, orientador, coorientador)`, numa só transação | P-03.9, P-03.10 |
| R8 | **Renumerar a lista** quando uma candidatura sai (cancelada, encerrada, recusada pelo colega ou contemplada): as seguintes sobem uma posição | Trigger AFTER UPDATE do estado da candidatura | P-03.3, P-03.6, P-03.10 |
| R9 | **Validar uma candidatura nova:** fase de candidaturas aberta, modalidade compatível, limite de candidaturas, créditos do aluno (e do colega). Sem créditos → estado Recusada; caso contrário fica na última posição | Trigger BEFORE INSERT da candidatura | P-03.1, P-03.2 |
| R10 | **Fechar no prazo:** depois do prazo de entrega, a entrega não pode ser alterada; depois do prazo de avaliação, a avaliação também não. Continuam disponíveis para consulta | Trigger BEFORE UPDATE em Entrega e em Avaliacao | P-05.3, P-06.6 |
| R11 | **Discrepância entre jurados:** ao submeter, se a diferença para outro jurado num critério for superior ao limiar, a justificação é obrigatória | Trigger BEFORE UPDATE da avaliação (passagem a Submetida) | P-06.6 |
| R12 | **Pesos e recálculo:** ao ativar o modelo, a soma dos pesos de cada destino tem de ser 100%. Acrescentar um outro momento recalcula os restantes, mantendo a proporção | Função `recalcular_pesos(momento)` e trigger na ativação do modelo | P-06.1, P-06.3 |
| R13 | **Calcular as notas:** nota do momento pela média dos jurados (níveis × 2, com os pesos dos critérios e a majoração) e nota final com os pesos dos momentos | Funções `calcular_nota_momento(tfc, momento)` e `calcular_resultado_final(tfc, epoca)` | P-07.1, P-07.2 |
| R14 | **Histórico:** cada mudança de estado, prioridade, nota ou dado publicado é registada em Historico, com o evento e o utilizador | Trigger AFTER UPDATE genérico nas tabelas principais | Todos |
| R15 | **Fechar o ano letivo:** arquiva os TFC e as propostas não atribuídas e passa o ano a só leitura | Função `fechar_ano_letivo(ano)` e trigger que bloqueia alterações em anos fechados | P-01.4 |

**Estado da implementação (17/11):** as restrições R1 a R6 e as regras R7, R8 e R9 estão implementadas e testadas no backend; R14 está implementada só para as candidaturas. As restantes (R10 a R13 e R15) ficam para as próximas iterações.

## 6. Vistas para o reporting

As consultas dos relatórios ficam em vistas da base de dados, para o backend e as exportações usarem sempre os mesmos dados. As primeiras são as que os docentes mais pediram no inquérito.

| Vista | Conteúdo | Processo |
|---|---|---|
| `vw_avaliacoes_pendentes` | Avaliações por submeter, por jurado e momento, com o prazo | P-09.3 (pedido por 7 em 8 docentes) |
| `vw_entregas_em_falta` | Entregas não submetidas ou com relatório por validar, por TFC e momento | P-09.3 |
| `vw_tfc_por_estado` | Número de TFC em cada estado, por ano letivo e orientador | P-09.3 |
| `vw_candidaturas_por_proposta` | Número de candidaturas por proposta e propostas sem candidatos | P-09.3 |
| `vw_alunos_sem_tfc` | Alunos elegíveis sem TFC atribuído e candidaturas recusadas por falta de créditos | P-09.3 |
| `vw_discrepancias_jurados` | Critérios com diferença entre jurados acima do limiar | P-09.3 |
| `vw_notas_por_criterio` | Classificações por critério, momento e TFC, de todos os anos | P-09.2 |

## 7. Lógica no backend

Fica no backend (Django) o que não é sobre a consistência dos dados:
- **Permissões:** quem pode ver e fazer o quê, conforme o perfil e a função no TFC (por exemplo, o aluno só vê os resultados publicados; o orientador vê sempre as avaliações dos TFC que orienta).
- **Ficheiros:** guardar o relatório na pasta e apagar o anterior; a base de dados só guarda o caminho.
- **Notificações:** criar e enviar as notificações e os emails (subsistema, P-09.4).
- **Exportações:** gerar os ficheiros Excel e PDF a partir das vistas da secção 6.
- **API:** expor os dados ao frontend e, se for essa a opção, ao DEISI2258.
- **Validações de formato:** links do vídeo e do repositório, tipo e tamanho dos ficheiros.

## 8. Rastreabilidade

| Macro-processo | Classes principais |
|---|---|
| MP-01 Configuração do ano letivo | AnoLetivo, Fase, Curso, GrupoCursos, UnidadeCurricular, Utilizador, Aluno, AlunoUC, InscricaoTFC, Docente, EntidadeExterna |
| MP-02 Gestão de propostas | Proposta, PropostaUC, Tecnologia, PropostaAluno, AnexoProposta, Historico |
| MP-03 Candidatura e atribuição | Grupo, Candidatura, Selecao, TFC, TFCAluno, Pedido |
| MP-04 Acompanhamento do TFC | Atividade, Pedido, TFCAluno |
| MP-05 Submissão de entregáveis | Entrega, VerificacaoAutomatica |
| MP-06 Avaliação | ModeloAvaliacao, MomentoAvaliacao, Criterio, MembroJuri, Defesa, Avaliacao, ClassificacaoCriterio |
| MP-07 Apuramento de resultados | NotaMomento, ResultadoFinal |
| MP-08 Seminários e DEISIFest | Seminario, Presenca, NotaMomento |
| MP-09 Consulta e notificações | Vistas da secção 6, Notificacao, Historico |

## 9. Questões em aberto

| # | Questão | Classes |
|---|---|---|
| 1 | Num grupo, as notas são sempre iguais para os dois alunos ou podem ser diferentes (por exemplo, na defesa final)? O modelo guarda uma nota por aluno, que serve para os dois casos. | NotaMomento, ResultadoFinal |
| 2 | As candidaturas individuais e em grupo de um aluno formam uma única lista de prioridades? Depende da questão 3 de [02_processos.md](02_processos.md). | Candidatura |
| 3 | Como chegam à base de dados os resultados da verificação do DEISI2258: escrita direta, ação a pedido no frontend ou tarefa do servidor em batch? A combinar com o DEISI2258. | VerificacaoAutomatica |
| 4 | Como entra a majoração do orientador no cálculo da nota? O modelo guarda o valor (inicialmente 0), mas a fórmula ainda não está definida. | ModeloAvaliacao, NotaMomento |
| 5 | O MP-08 passa a definir os modelos do modelo base de avaliação? O atributo `tipo` de MomentoAvaliacao já prevê os quatro modelos. | MomentoAvaliacao |
