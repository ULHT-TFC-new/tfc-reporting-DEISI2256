# Registo do Projeto — DEISI2256

Planeamento, registo de atividades e notas das reuniões do TFC.

---

## 1. Planeamento (até à 1.ª entrega intercalar)

| Período | Tarefa | Estado |
|---|---|---|
| 30/09 – 04/10 | Criar o repositório e coordenar com os grupos DEISI2257 e DEISI2258 | Em curso |
| 05/10 – 16/10 | Finalizar o inquérito e validá-lo com o orientador | Em curso |
| 19/10 – 06/11 | Divulgar o inquérito e recolher respostas | Em curso |
| 09/11 – 22/11 | Análise dos resultados e levantamento de requisitos | Por iniciar |
| 16/11 – 29/11 | Arquitetura, mockups e ambiente Docker | Por iniciar |
| 23/11 – 06/12 | Relatório e vídeo (máx. 2 min) | Por iniciar |

**Marcos:** 06/12/2026 envio do relatório ao orientador · 13/12/2026 1.ª entrega intercalar · 04/04/2027 2.ª entrega · 04/06/2027 entrega final · 07–19/06/2027 defesas

---

## 2. Diário de bordo

| Data | Atividade |
|---|---|
| 30/09/2026 | Exploração da plataforma de TFCs e primeiro esboço do questionário |
| 30/09/2026 | Reunião com o orientador (ver Reunião 1) |
| 30/09/2026 | Criação do repositório na organização ULHT-TFC-new |

---

## 3. Reuniões

### Reunião 1 — 30/09/2026

**Com:** Prof. Luís Gomes (orientador) e os grupos DEISI2257 e DEISI2258

**O que foi falado**
- Antes do levantamento de requisitos, fazer um inquérito aos utilizadores da plataforma atual, para saber o que mudar e melhorar.
- Dividir os inquiridos em três perfis: alunos que iniciaram o TFC, alunos que já o concluíram e docentes.
- Separar os perfis evita que a média de grupos com experiências diferentes não represente nenhum deles.
- Cada grupo cria o seu repositório na organização ULHT-TFC-new.
- Criar o repositório.
- Próximos passos: coordenar com os outros grupos a estrutura dos repositórios, a base de dados e o backend, e finalizar o inquérito e validá-lo com o orientador.

### Reunião 2 — 07/10/2026

**Com:** Prof. Luís Gomes (orientador) e os grupos DEISI2257

**O que foi falado**
- O orientador indicou o que corrigir, alterar e acrescentar ao inquérito.
- Os processos não foram discutidos nesta reunião, mas já estavam elaborados.

### Reunião 3 — 14/10/2026

**Com:** Prof. Luís Gomes (orientador) e os grupos DEISI2258

**O que foi falado**
- O orientador indicou o que corrigir, alterar e acrescentar aos processos.
- Aconselhou a criar um fluxo e uma sequência tendo em conta o tipo de trabalho que está a ser feito.
- O inquérito vai ser disponibilizado na aula do seminário do TFC da próxima semana para os alunos presentes em sala responderem.

### Reunião 4 — 21/10/2026

**Com:** Prof. Luís Gomes (orientador) e os grupos DEISI2257

**O que foi falado**
- O orientador disse-nos o que fazer a seguir às respostas do inquérito. Desenhar e planear a arquitetura, base de dados, classes, etc...
- O inquérito foi disponibilizado aos alunos na aula do seminário TFC.

### Reunião 5 — 28/10/2026

**Com:** Prof. Luís Gomes (orientador) e o colega do TFC DEISI2257

**O que foi falado**

O orientador reviu o documento de processos e indicou o que alterar e melhorar.

*Atores*
- O docente, o orientador e o jurado são o mesmo ator, com funções diferentes.
- O sistema não é um ator.

*Propostas*
- Separar «publicar» e «consultar» proposta em dois processos.
- No estado da proposta, trocar «publicada» por «disponível», por legibilidade.
- A proposta deve indicar se o TFC é individual ou em grupo, e esta caracterização deve poder ser filtrada: os trabalhos individuais não aceitam grupos.
- Os cursos devem vir de uma tabela de grupos de cursos (por exemplo LEI, LIG), escolhidos por checkbox.
- Na base de dados, os docentes têm de estar ativos ou inativos, para se saber se estão a trabalhar com TFC.

*Candidatura e atribuição*
- Separar «alterar» e «cancelar» candidatura em dois processos.
- Prever a candidatura recusada por falta de créditos, ao registar o TFC.
- Descrever o processo de submeter candidatura em grupo.
- Criar um processo para alterar o trabalho (de A para B).
- Prever a possibilidade de os docentes juntarem alunos para fazerem um TFC.

*Avaliação e apuramento de resultados*
- Definir os critérios e os momentos de avaliação.
- Prever uma avaliação adicional (quase certa).
- Dividir o apuramento em dois processos: o cálculo da nota de cada avaliação, incluindo a nota intercalar, e o cálculo da nota final.

*Documentação*
- Acrescentar diagramas de sequência e de workflow aos processos.

**Próximos passos**
- Atualizar o documento de processos com estas alterações.

  
### Reunião 6 — Feedback e Revisão do Documento de Processos

**Com:** Prof. Luís Gomes (orientador) e o grupo de TFC DEISI 2257 e DEISI 2258

**O que foi falado**

* **Análise dos Resultados do Inquérito**
  * Registaram-se 60 respostas no total (48 de alunos e 8 de docentes), o que representa uma amostra muito significativa (cerca de dois terços dos alunos inscritos nos últimos 2 anos).

* **Atores e Proponentes Externos**
  * O proponente externo deve manter a flexibilidade para abranger tanto empresas/instituições parceiras como docentes de outros departamentos da faculdade.

* **MP-01 — Configuração do Ano Letivo e Histórico**
  * Adicionar o processo de **fecho do ano anterior**: o fecho passa os dados do ano letivo anterior para histórico (consultável em base de dados, mas não ativo no momento).
  * O sistema deve guardar o histórico de todos os anos letivos, apresentando por defeito o ano atual com opção de retroceder para anos anteriores.

* **MP-03 — Candidatura e Atribuição**
  * **Candidaturas de Grupo (P-03.1, P-03.3, P-03.4):** Clarificar a mecânica de validação/confirmação. O fluxo deve prever que o segundo elemento do grupo confirma a candidatura submetida pelo submissor.
  * **Substituição de TFC (P-03.6 vs. P-03.7 + P-03.2):** Avaliar a pertinência técnica e operacional de manter o processo explícito de "substituir TFC da candidatura" na mesma prioridade em alternativa ao fluxo de cancelar e voltar a inscrever no fim da lista.

* **MP-06 — Avaliação e Critérios**
  * **Desdobrar o P-06.1:** Separar em dois processos distintos: *Definição de momentos de avaliação* e *Definição de critérios de avaliação* (pois um mesmo momento de avaliação contém múltiplos critérios ponderados, como originalidade, relatório, etc.).
  * **Momentos adicionais de avaliação:** Definir de forma abstrata como contam outros momentos (ex.: seminários ou apresentações parcelares), cuja ponderação pode ser global para o apuramento final ou direcionada a um momento específico.

* **MP-09 — Consultas, Notificações e Acessos**
  * **Notificações:** Não podem ser apenas uma linha estática; devem ser especificadas como um subsistema completo a integrar na arquitetura técnica.
  * **Consulta de resultados:** Adicionar explicitamente o processo de *Consultar Resultados* (separando a publicação de resultados parciais/intercalares dos finais).
  * **Acesso do Orientador às Avaliações:** O orientador deve ter acesso permanente e histórico a todas as avaliações e notas dos trabalhos que orienta, impedindo que perca o acesso às avaliações antigas após uma nova entrega.

* **Modelação de Estados (Diagramas Mermaid)**
  * Criar **Máquinas de Estados (*State Machines*)** em Mermaid para representar os ciclos de vida das propostas e das candidaturas.
  * Garantir que todas as transições de estado possuem um evento disparador (*trigger*) explícito (ex.: o estado passar de `ACEITE` a `DISPONÍVEL` mediante o evento de *Publicar*).

* **Formatação e Referências ao Regulamento**
  * Evitar a inclusão de texto bruto ou genérico que aparente ter sido gerado diretamente por IA sem revisão.
  * Em vez de colar o articulado do regulamento, fazer citações/referências diretas aos pontos do regulamento no corpo do texto e incluir a ligação oficial nas referências bibliográficas do relatório.

**Próximos passos**

1. Reformular o documento de processos aplicando todas as correções indicadas.
2. Gerar os diagramas de *State Machine* em Mermaid para propostas e candidaturas.
3. Derivar os microprocessos para **Casos de Uso (Use Cases)** e **User Stories** em modelo ágil (definindo atores, pré-condições, pós-condições e critérios de aceitação).
4. Enviar o link do *commit* do Git com os registos de reunião ao orientador.

**Decisões iniciais**
- Inquérito com ramificação por perfil (cada perfil responde apenas aos blocos que lhe dizem respeito).
