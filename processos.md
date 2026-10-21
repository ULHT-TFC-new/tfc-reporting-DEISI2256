# 02 — Macro-processos e processos

Estrutura do método de ERT: **macro-processos** (grandes áreas e objetivo) → **processos** (mezzo) → **descrição detalhada** (micro). Os macro-processos seguem a ordem do ano letivo e, dentro de cada um, os processos seguem a ordem de execução. A descrição detalhada cobre a configuração do ano letivo (calendário e modelo de avaliação), o registo de temas, a candidatura, a atribuição e a submissão de entregáveis; os restantes processos estão descritos em linhas gerais.

## 1. Atores

| Ator | Descrição |
|---|---|
| Aluno | Inscrito na UC de TFC, individualmente ou em grupo de 2 |
| Docente | Docente do DEISI: proponente, orientador ou jurado |
| Orientador / Coorientador | Papéis atribuídos por TFC; o coorientador pode ser externo |
| Jurado | Avalia o TFC (nas intercalares é externo ao trabalho) |
| Coordenação | Coordenação de TFC |
| Proponente externo | Docente de outro departamento ou empresa/instituição parceira |
| Organização de seminários | Valida as presenças |
| Administrador | Gestão técnica da plataforma |
| Sistema | Prazos, cálculos, verificações e notificações automáticos |

O acesso depende do **perfil da conta** e do **papel no TFC** (um docente pode ser proponente num TFC, orientador noutro e jurado noutro).

## 2. Macro-processos

| ID | Macro-processo | Objetivo | Atores principais |
|---|---|---|---|
| MP-01 | Configuração do ano letivo | Definir prazos, utilizadores e modelo de avaliação sem alterar a plataforma | Coordenação |
| MP-02 | Gestão de propostas (registo de temas) | Só publicar temas validados e com esforço adequado | Docente, Aluno, Proponente externo, Coordenação |
| MP-03 | Candidatura e atribuição | Atribuir os TFC aos alunos de forma justa, transparente e dentro dos prazos | Aluno, Proponente, Coordenação |
| MP-04 | Acompanhamento do TFC | Registar a evolução e as alterações ao longo do ano | Aluno, Orientador |
| MP-05 | Submissão de entregáveis | Entregas completas, validadas pelo orientador e dentro do prazo | Aluno, Orientador |
| MP-06 | Avaliação | Avaliações individuais, rastreáveis e, nas intercalares, cegas | Jurado, Coordenação |
| MP-07 | Apuramento de resultados | Calcular a nota final de forma automática e auditável | Sistema, Coordenação |
| MP-08 | Seminários e DEISIFest | Controlar obrigações que não são entregas | Organização, Coordenação |
| MP-09 | Consulta e notificações | Dar a cada perfil a informação de que precisa | Todos |

## 3. Processos (nível mezzo)

### MP-01 — Configuração do ano letivo

| ID | Processo | Ator | Descrição |
|---|---|---|---|
| P-01.1 | Definir calendário e épocas de avaliação | Coordenação | Registar as fases do ano (propostas, candidaturas, publicação, entregas, defesas) com início e fim; o sistema abre e fecha as funcionalidades. |
| P-01.2 | Gerir utilizadores e perfis | Coordenação, Administrador | Registar alunos inscritos na UC (número, curso, ECTS, UCs concluídas), docentes e entidades externas e atribuir perfis. |
| P-01.3 | Configurar modelo de avaliação | Coordenação | Definir os momentos de avaliação e os seus pesos, os critérios e pesos de cada momento, a escala de classificação e as regras de apuramento de resultados. |

### MP-02 — Gestão de propostas (registo de temas)

| ID | Processo | Ator | Descrição |
|---|---|---|---|
| P-02.1 | Submeter proposta | Docente, Aluno, Proponente externo | Propor um tema com curso, disciplinas e tecnologias, e perfil de candidato ou alunos pré-selecionados. |
| P-02.2 | Validar proposta | Coordenação | Aceitar, pedir alterações ou recusar uma proposta e nomear o orientador. |
| P-02.3 | Rever proposta | Proponente | Alterar uma proposta após pedido de alterações. |
| P-02.4 | Publicar e consultar propostas | Sistema, todos | Disponibilizar as propostas aceites, listá-las e mostrar o detalhe; o proponente vê as suas propostas. |

### MP-03 — Candidatura e atribuição

| ID | Processo | Ator | Descrição |
|---|---|---|---|
| P-03.1 | Formar grupo | Aluno | Constituir um grupo de 2 alunos, com confirmação do colega. |
| P-03.2 | Submeter candidatura | Aluno | Candidatar-se a um TFC com uma prioridade na lista de inscrições. |
| P-03.3 | Confirmar candidatura de grupo | Colega de grupo | O colega confirma ou recusa a candidatura submetida pelo submissor. |
| P-03.4 | Alterar ou cancelar candidatura | Aluno | Reordenar ou remover candidaturas dentro do prazo. |
| P-03.5 | Selecionar candidatos | Proponente, Coordenação, Sistema | Escolher o candidato de cada TFC quando há mais de um. |
| P-03.6 | Atribuir TFC e orientador | Sistema, Coordenação | Atribuir o TFC ao aluno ou grupo e nomear orientador e coorientador. |
| P-03.7 | Atualizar listas de candidaturas após atribuição | Sistema | Retirar o TFC atribuído das listas dos outros candidatos e subir as prioridades seguintes. |
| P-03.8 | Publicar atribuições | Coordenação | Publicar a lista final de TFC atribuídos e orientadores. |
| P-03.9 | Registar desistência e libertar TFC | Aluno, Orientador, Coordenação | Registar a desistência de um aluno e libertar o TFC: volta à lista de inscrições se o período de candidaturas estiver aberto; caso contrário, fica disponível para atribuição pela coordenação. |

### MP-04 — Acompanhamento do TFC

| ID | Processo | Ator | Descrição |
|---|---|---|---|
| P-04.1 | Registar repositório e atividades | Aluno, Orientador | Associar o link do repositório Git e registar atividades e reuniões. |
| P-04.2 | Dissociar grupo | Orientador, Coordenação | Separar um grupo quando não há equilíbrio de esforço; as avaliações já feitas não se repetem. |
| P-04.3 | Pedir adiamento para época de recurso | Aluno, Orientador, Coordenação | Adiar a entrega final para a época de recurso, com parecer favorável do orientador. |

### MP-05 — Submissão de entregáveis

| ID | Processo | Ator | Descrição |
|---|---|---|---|
| P-05.1 | Enviar relatório ao orientador | Aluno | Enviar o relatório em PDF para validação, com antecedência mínima. |
| P-05.2 | Validar relatório | Orientador | Aceitar ou devolver o relatório e informar a coordenação. |
| P-05.3 | Submeter entrega | Aluno | Submeter o relatório em PDF e as ligações dos restantes entregáveis de cada momento. |

### MP-06 — Avaliação

| ID | Processo | Ator | Descrição |
|---|---|---|---|
| P-06.1 | Constituir júri | Coordenação | Definir o júri de cada TFC e momento (júri cego nas intercalares). |
| P-06.2 | Agendar defesas | Coordenação | Marcar e publicar as defesas finais com pelo menos 48 h de antecedência; TFC com AND não são gravados nem divulgados. |
| P-06.3 | Preencher formulário de avaliação | Jurado | Classificar cada critério (Likert 1–10) e escrever a apreciação; justificação obrigatória se a discrepância entre jurados for superior a 2 níveis. |
| P-06.4 | Publicar resultados | Coordenação | Disponibilizar notas e apreciações aos alunos (intercalares até 10 dias úteis após o prazo). |

### MP-07 — Apuramento de resultados

| ID | Processo | Ator | Descrição |
|---|---|---|---|
| P-07.1 | Calcular nota final e situação | Sistema, Coordenação | Aplicar as regras do modelo de avaliação (P-01.3; em 2026/27: AI1 20%, AI2 20%, AF 55%, DF 5%), arredondar à unidade e determinar aprovado, reprovado ou excluído, tendo também em conta o cumprimento dos seminários (P-08.1). |

### MP-08 — Seminários e DEISIFest

| ID | Processo | Ator | Descrição |
|---|---|---|---|
| P-08.1 | Registar presenças em seminários | Organização, Coordenação | Registar presenças individuais; o aluno cumpre com pelo menos 70% dos seminários do ano. |
| P-08.2 | Registar resultado do DEISIFest | Coordenação | Registar a média das votações de cada trabalho (5% da nota final). |

### MP-09 — Consulta e notificações

| ID | Processo | Ator | Descrição |
|---|---|---|---|
| P-09.1 | Consultar estado do TFC | Aluno, Orientador | Ver o TFC, os prazos, o estado das entregas e as pendências. |
| P-09.2 | Consultar relatórios de gestão | Coordenação | Ver propostas, candidaturas, alunos sem TFC, entregas em atraso e avaliações por lançar. |
| P-09.3 | Receber notificações | Todos | Receber avisos na plataforma e por e-mail dos eventos relevantes. |

## 4. Descrição detalhada (nível micro)

Cada ficha indica pré-condições, fluxo, exceções e regras. `[UI]` indica comportamento observado na plataforma atual; as regras citam o capítulo do regulamento.

### 4.1 MP-01 — Configuração do ano letivo

**P-01.1 Definir calendário e épocas de avaliação** — *Coordenação*
- **Pré-condições:** perfil Coordenação.
- **Fluxo:**
  1. a coordenação cria as fases do ano (propostas, candidaturas, publicação, entregas, defesas) com início e fim;
  2. o sistema valida a coerência das datas;
  3. a coordenação publica o calendário;
  4. o sistema abre e fecha as funcionalidades de acordo com as datas.
- **Exceções:** alterar uma data com submissões já feitas pede confirmação e fica registado; sem época de avaliação ativa, a entrega mostra "Não existe nenhuma época de avaliação disponível" `[UI]`.
- **Regras:** o servidor valida sempre a janela; as datas do ano letivo são as da secção 5 deste documento (regulamento, "Datas importantes") e podem ser alteradas.

**P-01.3 Configurar modelo de avaliação** — *Coordenação*
- **Pré-condições:** perfil Coordenação; ano letivo criado (P-01.1).
- **Fluxo:**
  1. a coordenação define os momentos de avaliação e o peso de cada um na nota final;
  2. para cada momento com júri, define os critérios e o peso de cada critério;
  3. define a escala de classificação, o limiar de discrepância entre jurados que obriga a justificação e as regras de arredondamento;
  4. o sistema valida as somas dos pesos e ativa o modelo para o ano letivo.
- **Exceções:** soma dos pesos diferente de 100% → bloquear a ativação; alterar um momento que já tem avaliações registadas → criar uma nova versão do modelo, sem alterar as avaliações já feitas.
- **Regras (cap. 5 e 6):** em 2026/27: AI1 20%, AI2 20%, AF 55%, DF 5%; critérios e pesos das intercalares e da final do cap. 5; escala Likert de 10 níveis; justificação obrigatória com discrepância superior a 2 níveis; notas parciais arredondadas a 2 casas decimais e nota final à unidade; aprovação com nota final ≥ 10. O modelo tem versões e cada avaliação fica associada à versão usada. A conversão da escala de 10 níveis para 0–20 está *por confirmar*.

### 4.2 MP-02 — Gestão de propostas (registo de temas)

**Estados da proposta:** `SUBMETIDA` → `EM_VALIDAÇÃO` ↔ `ALTERAÇÕES_SOLICITADAS` → `ACEITE` ou `RECUSADA`; `ACEITE` → `PUBLICADA` (disponível, "A Aguardar Atribuição" `[UI]`) ou `PRÉ_ATRIBUÍDA` (tem aluno indicado); `PRÉ_ATRIBUÍDA` → `ATRIBUÍDA` (depois da candidatura do(s) aluno(s) pré-selecionado(s)); `PUBLICADA` → `ATRIBUÍDA` → `PUBLICADA` (se houver desistência com o período de candidaturas aberto).

**P-02.1 Submeter proposta** — *Docente, Aluno, Proponente externo*
- **Pré-condições:** autenticado; janela do seu tipo de proponente aberta; aluno inscrito na UC.
- **Dados:** título, descrição, empresa/entidade, orientador (preferencial ou sugerido), curso(s), disciplina(s), tecnologia(s) `[UI]`; e aluno(s) pré-selecionado(s) **ou** perfil do candidato (curso e UCs concluídas ou em curso); 2.º aluno, se for grupo.
- **Fluxo:**
  1. o proponente preenche o formulário do seu tipo;
  2. o sistema valida os campos obrigatórios;
  3. proposta de **docente DEISI sem aluno indicado** → fica `ACEITE` e publicada; as restantes → `SUBMETIDA`;
  4. o sistema notifica a coordenação (e o 2.º aluno, se for grupo).
- **Exceções:** janela fechada → formulário indisponível; sem perfil nem pré-seleção → bloquear; 2.º aluno já noutro grupo → bloquear.
- **Regras (regulamento, cap. 3):** o aluno pode submeter várias propostas; a proposta de grupo é submetida por um só elemento; o orientador preferencial indicado pelo aluno exige aprovação prévia dele (senão a proposta pode ser excluída); empresas e outros departamentos podem ser coorientadores.

**P-02.2 Validar proposta** — *Coordenação*
- **Pré-condições:** proposta `SUBMETIDA` ou `EM_VALIDAÇÃO`.
- **Fluxo:**
  1. a coordenação abre a lista de propostas por validar; ao abrir uma proposta `SUBMETIDA`, esta passa a `EM_VALIDAÇÃO`;
  2. analisa tema, esforço, enquadramento e disponibilidade do orientador;
  3. **aceita**, **pede alterações** (com mensagem) ou **recusa** (justificação obrigatória);
  4. se aceitar, pode acrescentar tarefas ou requisitos e nomear orientador e coorientador;
  5. o sistema atualiza o estado e notifica o proponente. Aceite sem pré-seleção → `PUBLICADA`; com pré-seleção → `PRÉ_ATRIBUÍDA`.
- **Regras (cap. 2 e 3):** nas propostas de departamentos e empresas a coordenação nomeia o orientador por área científica (o sugerido é considerado e pode ser substituído); limite sugerido de 5 orientações por docente (aviso); o histórico de estados fica registado.

**P-02.3 Rever proposta** — *Proponente*
- **Fluxo:** com a proposta em `ALTERAÇÕES_SOLICITADAS`, o proponente lê o pedido, edita e reenvia; volta a `EM_VALIDAÇÃO`.
- **Exceções:** fora da janela → só leitura.

**P-02.4 Publicar e consultar propostas** — *Sistema, todos*
- **Fluxo:**
  1. as propostas aceites sem pré-seleção passam a `PUBLICADA`;
  2. a listagem mostra ID, título e orientador/coorientador, com pesquisa por orientador `[UI]`;
  3. o detalhe mostra empresa, orientador, título, descrição, estado, curso, disciplinas e tecnologias `[UI]`;
  4. o proponente vê as suas propostas e o estado de cada uma; sem propostas aparece "Ainda não submeteu nenhum tema para TFC" `[UI]`.
- **Regras:** um TFC pré-atribuído só aparece ao(s) aluno(s) pré-selecionado(s), para fazerem a candidatura formal (P-03.2); não aparece aos restantes alunos.

### 4.3 MP-03 — Candidatura e atribuição

Os processos estão descritos **pela ordem de execução**: formar grupo → candidatar-se → confirmação do colega (se for grupo) → gerir a lista → selecionar → atribuir → atualizar as listas dos outros candidatos → publicar. A desistência (P-03.9) pode ocorrer depois da atribuição e devolve o TFC à lista de disponíveis.

**Estados da candidatura**

| Estado | Significado | Aparece na lista de inscrições? |
|---|---|---|
| `PENDENTE_CONFIRMAÇÃO` | Candidatura de grupo submetida; o colega ainda não confirmou | Sim, com aviso |
| `ATIVA` | Válida e a concorrer | Sim |
| `CONTEMPLADA` | O TFC foi atribuído a este aluno ou grupo | Não (passa a ser o seu TFC) |
| `ENCERRADA` | Terminou sem atribuição, com motivo: TFC atribuído a outro; aluno já contemplado; recusada pelo colega; sem confirmação a tempo; anulada por novo grupo | Não (fica no histórico) |
| `CANCELADA` | Retirada pelo aluno | Não (fica no histórico) |

**Lista de inscrições:** contém as candidaturas `PENDENTE_CONFIRMAÇÃO` e `ATIVA`, com prioridade de 1 a n, sem lacunas. Sempre que uma candidatura sai da lista, as seguintes **sobem uma posição**.

**P-03.1 Formar grupo** — *Aluno*
- **Pré-condições:** os dois alunos inscritos na UC, elegíveis (≥ 90 ECTS, referência 04.10.2026) e sem grupo ativo; janela de candidaturas aberta.
- **Fluxo:**
  1. o aluno indica o número do 2.º aluno;
  2. o sistema valida (inscrito, elegível, sem grupo);
  3. o sistema avisa que formar o grupo **anula as candidaturas anteriores** de ambos e pede confirmação;
  4. o sistema envia o convite ao colega;
  5. o colega **confirma**;
  6. o sistema ativa o grupo, fixa o **submissor** (quem convidou) e anula as candidaturas anteriores de ambos.
- **Exceções:** colega recusa → grupo não se forma e o aluno mantém as suas candidaturas; colega já noutro grupo → bloquear; colega não elegível → informar; janela fechada → indisponível.
- **Regras (cap. 4):** cada aluno só pode estar num grupo; só o submissor cria e altera candidaturas do grupo.

**P-03.2 Submeter candidatura** — *Aluno (individual ou submissor do grupo)*
- **Pré-condições:** aluno elegível; janela aberta; TFC `PUBLICADA`, ou `PRÉ_ATRIBUÍDA` quando o aluno é o pré-selecionado; limite de candidaturas não atingido.
- **Fluxo:**
  1. o aluno abre o detalhe do TFC, que mostra o número de inscrições atuais;
  2. carrega em **Inscrever**;
  3. o sistema valida elegibilidade, disponibilidade do TFC, janela, limite e duplicação;
  4. o sistema regista a candidatura na última posição da lista, com **data e hora**;
  5. **individual** → `ATIVA`; **grupo** → `PENDENTE_CONFIRMAÇÃO` e o colega é notificado (P-03.3).
- **Exceções:** limite atingido → botão desativado e mensagem "retire uma inscrição de outro TFC" `[UI]`; requisito em falta → mensagem a indicar qual; TFC atribuído entretanto → bloquear.
- **Regras (cap. 3 e 4):** 3 a 6 TFC por ordem de preferência (a plataforma atual bloqueia aos 5; o limite é parametrizável); mesmo com pré-seleção, a candidatura na plataforma é obrigatória, porque a atribuição formal é necessária para a avaliação.

**P-03.3 Confirmar candidatura de grupo** — *Colega de grupo*
- **Pré-condições:** grupo ativo; candidatura `PENDENTE_CONFIRMAÇÃO`; janela aberta.
- **Fluxo:**
  1. o sistema notifica o colega de que o submissor se candidatou a um TFC em nome do grupo;
  2. o colega abre a candidatura e o detalhe do TFC;
  3. carrega em **Confirmar**;
  4. o sistema revalida (TFC disponível, janela aberta, colega elegível para o perfil);
  5. a candidatura passa a `ATIVA`, na mesma posição;
  6. o sistema notifica o submissor.
- **Alternativas:** o colega **recusa** → `ENCERRADA` (recusada), sai da lista e as seguintes sobem uma posição; sem resposta até ao fecho da janela → `ENCERRADA` (sem confirmação).
- **Regras:** uma candidatura pendente não entra na seleção; só o colega a pode confirmar.

**P-03.4 Alterar ou cancelar candidatura** — *Aluno (submissor, se for grupo)*
- **Fluxo:**
  1. na "Lista de Inscrições" (ID, título, orientador, prioridade; pesquisa por orientador e por ordem) `[UI]` o aluno vê as suas candidaturas;
  2. reordena ou remove uma candidatura (a remoção pede confirmação);
  3. o sistema renumera de 1 a n, sem lacunas.
- **Exceções:** janela fechada → só leitura; menos de 3 candidaturas → aviso.
- **Regras:** em grupo só o submissor altera e o colega consulta.

**P-03.5 Selecionar candidatos** — *Proponente, Coordenação, Sistema*
- **Pré-condições:** fim das candidaturas; TFC com um ou mais candidatos `ATIVA` (as pendentes não entram).
- **Fluxo:**
  1. o sistema lista os candidatos de cada TFC com média, notas nas UCs do perfil, prioridade dada ao TFC e data de inscrição;
  2. **com proponente**, este escolhe (pode entrevistar os candidatos fora da plataforma); **sem proponente**, o sistema ordena por (1) resultados nas UCs do perfil e (2) cronologia da inscrição;
  3. o sistema propõe as atribuições e permite **simular** o resultado, sem efeitos;
  4. a coordenação revê, ajusta se necessário (com justificação) e confirma.
- **Exceções:** TFC sem candidatos → "A Aguardar Atribuição" `[UI]`; aluno sem TFC no fim → atribuição manual pela coordenação, com justificação.
- **Regras (cap. 4):** quem tem tema próprio e candidaturas: (1) candidaturas a temas de docentes ou empresas, pela ordem indicada, (2) temas de docentes ou empresas que sobreponham o tema próprio, (3) o tema próprio.

**P-03.6 Atribuir TFC e orientador** — *Sistema, Coordenação*
- **Fluxo:**
  1. a atribuição é **automática** quando há pré-seleção de alunos elegíveis que fizeram a candidatura (P-03.2), ou quando o aluno só tem tema próprio aceite; caso contrário vem da seleção confirmada (P-03.5);
  2. a coordenação nomeia orientador e coorientador (o sugerido na proposta aparece por defeito);
  3. o TFC passa a `ATRIBUÍDA` e a candidatura do aluno a `CONTEMPLADA`;
  4. as restantes candidaturas do aluno contemplado ficam `ENCERRADA` (aluno já contemplado);
  5. o sistema executa P-03.7;
  6. o sistema notifica aluno(s), orientador e coorientador.
- **Exceções:** pré-selecionado sem elegibilidade → alerta; aluno pré-selecionado em dois TFC → decide a coordenação; orientador acima do limite sugerido de 5 → aviso, não bloqueio.
- **Regras (cap. 2, 4 e 5):** cada aluno só pode ter um TFC; o aluno começa o trabalho logo que lhe é atribuído tema, mesmo antes da lista final.

**P-03.7 Atualizar listas de candidaturas após atribuição** — *Sistema*
- **Pré-condições:** um TFC passou a `ATRIBUÍDA` e existem candidaturas de outros alunos a esse TFC (ativas ou pendentes).
- **Fluxo:**
  1. o sistema identifica as candidaturas ao TFC atribuído feitas por alunos que não são os contemplados;
  2. cada uma passa a `ENCERRADA` (TFC atribuído a outro), guardando a posição *k* que tinha;
  3. em cada lista afetada, as candidaturas com posição superior a *k* **sobem uma posição**; a lista fica de 1 a n − 1, sem lacunas;
  4. o sistema regista a posição anterior e a nova;
  5. se o aluno ficar com menos de 3 candidaturas, vê um aviso (janela aberta) ou a coordenação é alertada (janela fechada);
  6. o sistema notifica cada aluno afetado: TFC retirado e nova ordem.
- **Exemplo:** a lista de um aluno é 1 TFC A · 2 TFC B · 3 TFC C · 4 TFC D. O TFC B é atribuído a outro aluno. A lista passa a 1 TFC A · 2 TFC C (antes 3) · 3 TFC D (antes 4).
- **Exceções:** falha a meio → nenhuma lista fica parcialmente atualizada; o aluno estava a editar a lista (P-03.4) → a atualização do sistema prevalece e o aluno é avisado.
- **Regras:** mantém-se a ordem relativa das restantes candidaturas; a data/hora de inscrição não muda.

**P-03.8 Publicar atribuições** — *Coordenação*
- **Fluxo:** a coordenação revê e publica a lista final (TFC, aluno(s), orientador); o sistema notifica os atribuídos e encerra o período de candidaturas.
- **Exceções:** correções posteriores ficam registadas e notificadas.

**P-03.9 Registar desistência e libertar TFC** — *Aluno, Orientador, Coordenação*
- **Pré-condições:** TFC `ATRIBUÍDA` com o aluno associado.
- **Fluxo:**
  1. o aluno pede a desistência e indica o motivo;
  2. o sistema mostra as consequências e pede confirmação;
  3. o orientador regista o seu parecer;
  4. a coordenação valida;
  5. o sistema cancela a atribuição e guarda o histórico;
  6. com o período de candidaturas **aberto**, o TFC passa a `PUBLICADA` e **volta à lista de TFC disponíveis para inscrição**; com o período **fechado**, o TFC fica disponível apenas para atribuição pela coordenação (não são admitidos novos trabalhos depois da data-limite de candidaturas, regulamento cap. 1);
  7. o sistema notifica orientador, coorientador, proponente e coordenação.
- **Alternativas (grupo):** se um elemento desiste e o outro quer continuar a título individual, o TFC mantém-se atribuído ao remanescente com o âmbito ajustado pelo orientador; se nenhum continuar, aplica-se o passo 6.
- **Regras:** as candidaturas antigas do aluno não são repostas.

### 4.4 MP-05 — Submissão de entregáveis

**P-05.1 Enviar relatório ao orientador** — *Aluno*
- **Fluxo:** o aluno carrega a versão em PDF; o sistema verifica a antecedência mínima face ao prazo e notifica o orientador.
- **Regras:** antecedência parametrizável, por defeito 1 semana (regulamento, cap. 1, ponto 13); fora da antecedência há aviso e o relatório pode ser recusado.

**P-05.2 Validar relatório** — *Orientador*
- **Fluxo:** o orientador **valida** ou **devolve com comentários**; ao validar, a coordenação é informada e a entrega fica desbloqueada.
- **Regras (cap. 5):** só relatórios validados pelo orientador são aceites para avaliação.

**P-05.3 Submeter entrega** — *Aluno (submissor, se for grupo)*
- **Pré-condições:** relatório validado; época de avaliação ativa; dentro do prazo.
- **Fluxo:**
  1. o aluno abre "Entrega de artefactos" `[UI]` e vê a lista de entregáveis do momento (AI1, AI2 ou final) e o prazo;
  2. carrega o **PDF** do relatório e indica as **ligações** (repositório Git e vídeo; na entrega final, também a versão operacional);
  3. o sistema valida o formato e as ligações e guarda a versão com data;
  4. o sistema notifica orientador e coordenação.
- **Exceções:** prazo expirado → bloquear e registar falta; PDF acima do limite de tamanho → restringir e passar o resto para o Git; ligação de canal em vez de vídeo, ou ligação inacessível → alerta.
- **Regras (cap. 5 e anexo D):** entregáveis por momento — AI1: relatório e vídeo até 2 min; AI2: relatório, versão funcional no Git e vídeo até 5 min; final: relatório, texto de divulgação (máx. 10 linhas) e imagem, código-fonte no Git, versão operacional e vídeo até 5 min. O vídeo é indicado pela ligação do vídeo (não do canal), público e inalterado até à nota final. Todos os relatórios incluem o inquérito de IA generativa (anexo E).

## 5. Calendário 2026/27 (parametrizável)

| Fase | Datas |
|---|---|
| Propostas de docentes, departamentos e empresas | 01.09 – 30.09.2026 |
| Propostas de alunos / sua avaliação | 10.09 – 27.09 / 11.09 – 30.09.2026 |
| Candidaturas (data de referência da elegibilidade: 04.10) | 09.09 – 04.10.2026 |
| Lista final de atribuídos | 05.10.2026 |
| AI1: entrega / resultados | 13.12.2026 / 04.01.2027 |
| AI2: entrega / resultados | 04.04.2027 / 18.04.2027 |
| Entrega final 1.ª época / defesas | 04.06.2027 / 07 a 19.06.2027 |
| Entrega final 2.ª época / defesas | 02.07.2027 / 05 a 16.07.2027 |
