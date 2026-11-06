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

O orientador reviu o documento de processos e indicou o que alterar e melhorar. Foi também feito o ponto de situação do inquérito: as respostas começaram a chegar há 4 ou 5 dias e alguns alunos ainda não tinham respondido.

*Atores*
- O docente, o orientador e o jurado são o mesmo ator, com funções diferentes em cada TFC (proponente, orientador, coorientador ou jurado).
- O sistema não é um ator.
- Só os docentes ativos podem aparecer nas listas de seleção (orientador preferencial, orientador sugerido, nomeação pela coordenação e júri). Os inativos servem apenas para preservar e consultar o histórico.

*Propostas (MP-02)*
- Separar «publicar» e «consultar» proposta em dois processos.
- No estado da proposta, trocar «publicada» por «disponível», por legibilidade.
- A proposta tem uma de três modalidades, vinculativas: *Individual* (só aceita candidaturas individuais), *Em grupo* (só aceita candidaturas em grupo) e *Individual ou em grupo* (aceita ambas). Esta caracterização deve poder ser filtrada.
- O docente proponente pode alterar os dados de um TFC ainda não atribuído, desde que a alteração seja compatível com as candidaturas existentes. Mudar a modalidade para «em grupo» quando já há candidaturas individuais (ou o inverso) deve ser bloqueado ou condicionado.
- As propostas de docentes do DEISI sem aluno indicado ficam com o estado ACEITE e passam de imediato a DISPONÍVEL, sendo publicadas automaticamente na submissão.
- Os cursos devem vir de uma tabela de grupos de cursos (por exemplo LEI, LIG), escolhidos por checkbox.
- Na base de dados, os docentes têm de estar ativos ou inativos, para se saber se estão a trabalhar com TFC.

*Candidatura e atribuição (MP-03)*
- Separar «alterar» e «cancelar» candidatura em dois processos.
- Descrever o processo de submeter candidatura em grupo.
- Quando um aluno convida um colega para formar grupo, ou quando o docente junta dois alunos num TFC (P-03.9), ambos têm de aceitar. Não há submissões nem junções unilaterais válidas.
- Criar um processo para alterar o trabalho (de A para B).
- Prever a possibilidade de os docentes juntarem alunos para fazerem um TFC.
- Candidatura recusada por falta de créditos: se o aluno não tiver os créditos mínimos (≥ 90 ECTS à data de referência de 4 de outubro), o sistema recusa a submissão, regista-a com o estado RECUSADA (aluno, TFC, data e motivo) e mostra uma mensagem a explicar que não reúne os créditos exigidos. Estes registos podem ser consultados.
- Quando um TFC é atribuído a um aluno, desaparece das listas de inscrições dos outros candidatos e as prioridades seguintes sobem, sem lacunas. Se um aluno ficar com menos de 3 candidaturas ativas, o sistema mostra um aviso.
- Desistência (P-03.13): iniciada pelo aluno, com pedido fundamentado, parecer do orientador e validação da coordenação. Se o período de candidaturas estiver aberto, o TFC volta a DISPONÍVEL na lista geral. Se estiver fechado, o TFC só pode ser atribuído manualmente pela coordenação, porque não se admitem novos trabalhos depois do fecho.
- Desatribuição (P-03.14): iniciada obrigatoriamente pelo orientador e validada pela coordenação. Serve para corrigir atribuições e, se o período de candidaturas estiver aberto, o aluno pode voltar a alterar as suas candidaturas.

*Relatório e entregas (MP-05)*
- Antes de submeter formalmente um momento (AI1, AI2 ou Final), o aluno envia o relatório em PDF ao orientador com uma antecedência mínima, por omissão de 1 semana. O orientador valida-o ou devolve-o com comentários.
- Em trabalhos de grupo, qualquer elemento pode submeter os artefactos e o relatório já validado, sem validação adicional do colega no momento do envio.

*Avaliação e apuramento de resultados (MP-06 e MP-07)*
- Definir os critérios e os momentos de avaliação. Os momentos globais (AI1, AI2, Final, Defesa e Avaliação Adicional) devem estar separados dos critérios internos de cada momento.
- Prever uma avaliação adicional (quase certa). Se existir, o seu peso é fixo e definido na criação, e os pesos dos restantes momentos são recalculados automaticamente, de forma proporcional.
- Dividir o apuramento em dois processos: o cálculo da nota de cada avaliação, incluindo a nota intercalar, e o cálculo da nota final.
- Os jurados avaliam por níveis (escala de 1 a 10), convertidos para a escala de 0 a 20 por regra de três: nota = nível × 20 / 10.
- A nota de cada momento é a média aritmética das avaliações submetidas pelos jurados (2 a 4 jurados).
- A majoração do orientador é um parâmetro do modelo, com valor inicial 0.
- Se as notas de dois jurados diferirem em mais de 2 níveis, o jurado tem de justificar a sua avaliação.
- A nota final é arredondada às unidades. Para aprovar, o aluno precisa de nota final ≥ 10 valores e de pelo menos 70% de assiduidade nos seminários.

*Seminários e DEISIFest (MP-08)*
- O controlo dos seminários é feito pela Organização de Seminários e pela Coordenação, com registo individual de presenças para verificar o mínimo de 70% de assiduidade.
- No DEISIFest, a média das votações obtidas pelos trabalhos conta 5% da nota final do TFC e tem de entrar no apuramento de resultados.

*Mensagens da interface*

A plataforma atual mostra mensagens que devem ser previstas nos processos:
- «Não existe nenhuma época de avaliação disponível» (ao tentar submeter fora de época).
- «Ainda não submeteu nenhum tema para TFC» (no painel do proponente sem propostas).
- «A Aguardar Atribuição» (para propostas aceites sem aluno pré-selecionado).

*Documentação*
- Acrescentar diagramas de sequência e de workflow aos processos.
- Rigor na separação de conceitos, na nomenclatura e na clareza dos estados.
- Os diagramas têm de refletir a realidade operacional: nas candidaturas de grupo e nas junções de alunos, mostrar a comunicação mútua (ambos aceitam). Na desistência e na desatribuição, mostrar o comportamento com o período de candidaturas aberto e fechado.

### Reunião 6 — 04/11/2026

**Com:** Prof. Luís Gomes (orientador) e os grupos DEISI2257 e DEISI2258

**O que foi falado**

*Análise dos resultados do inquérito*
- Registaram-se 60 respostas no total: 48 de alunos do ano letivo em curso, 4 de alunos de anos anteriores e 8 de docentes. Os inquéritos eram particularizados por perfil, pelo que as respostas das três audiências não podem ser agregadas.
- **Alunos do ano em curso:** as 48 respostas correspondem a cerca de 60% dos aproximadamente 80 alunos inscritos por ano, uma taxa de resposta boa. Estas respostas são relevantes e serão tratadas.
- **Docentes:** as 8 respostas (cerca de 30%) são poucas, pelo que serão consideradas indicativas, mas não significativas.
- **Alunos de anos anteriores:** as 4 respostas (cerca de 5% de um ano) não têm significado estatístico e não serão tratadas.

*Atores e proponentes externos*
- O proponente externo deve manter a flexibilidade para abranger empresas e instituições parceiras, bem como docentes de outros departamentos da faculdade.
- Distinguir os tipos de proponentes externos (por exemplo, empresas e outros departamentos da universidade), que na plataforma atual têm formulários diferentes.

*Configuração do ano letivo e histórico (MP-01)*
- Acrescentar o processo de **fecho do ano anterior**: os dados do ano letivo anterior passam para histórico, que continua consultável na base de dados mas deixa de estar ativo.
- O sistema guarda o histórico de todos os anos letivos, mostra por defeito o ano atual e permite recuar para anos anteriores.

*Candidatura e atribuição (MP-03)*
- **Retirar o P-03.1 (formar grupo):** repete o que já está na candidatura em grupo e na sua confirmação (P-03.3 e P-03.4). Na candidatura em grupo, o aluno que submete identifica os dois elementos e o segundo elemento confirma ou recusa.
- Foram admitidas duas opções para a confirmação do segundo elemento: confirmar o grupo uma única vez (ficando confirmadas todas as candidaturas do grupo) ou confirmar cada candidatura. Ficou decidido que o segundo elemento confirma cada uma das candidaturas do grupo, aceitando-a ou recusando-a.
- **Substituição de TFC (P-03.6 vs. P-03.7 + P-03.2):** substituir uma candidatura equivale a cancelar, candidatar-se de novo e reordenar, e os dois caminhos são válidos. O grupo decide se mantém o processo explícito de substituição, tendo em conta o trabalho de implementação e a alternativa de cancelar e voltar a inscrever no fim da lista.
- Uniformizar a nomenclatura: usar sempre «candidatura» ou sempre «inscrição».
- No diagrama de atribuição, não é necessário notificar os outros candidatos.

*Avaliação e critérios (MP-06)*
- Cada entrega tem um prazo limite. Depois dele, deixa de ser possível entregar, submeter ou alterar avaliações, mas as avaliações continuam sempre disponíveis para consulta.
- **Desdobrar o P-06.1** em dois processos: *Definição de momentos de avaliação* e *Definição de critérios de avaliação*. Cada momento tem uma data, um peso e um mecanismo de avaliação, e vários critérios com pesos próprios, como originalidade ou relatório (por exemplo, a entrega de 13/12 tem 7 critérios).
- **Outros momentos de avaliação:** criar um processo genérico, não limitado a seminários. Pode ser, por exemplo, um seminário de presença obrigatória sem nota ou uma defesa com nota. A nota pode contar para a nota final ou apenas para um momento específico (por exemplo, as apresentações de dezembro contam só para a 1.ª entrega).

*Resultados, consultas e notificações (MP-09)*
- **Notificações:** não podem ser apenas uma linha estática. Devem ser especificadas como um subsistema completo, a integrar na arquitetura técnica.
- **Consulta de resultados:** acrescentar explicitamente o processo *Consultar Resultados*. A publicação de resultados deve abranger também o apuramento final, e não só as avaliações intercalares, separando os resultados parciais dos finais.
- **Acesso do orientador às avaliações:** o orientador deve poder consultar sempre, incluindo o histórico, as avaliações e notas dos trabalhos que orienta. Hoje só vê as avaliações da última entrega, e deixa de ver as antigas depois de uma nova entrega.

*Estados e diagramas (Mermaid)*
- Modelar os ciclos de vida das propostas e das candidaturas como **máquinas de estados** (*state machines*) em Mermaid, e não como fluxogramas.
- Cada transição tem de ter um evento disparador (*trigger*) explícito. Por exemplo, `ACEITE` e `DISPONÍVEL` distinguem-se porque há um evento entre eles (*Publicar*).
- Os estados «submetida» e «em validação» da proposta não têm um evento que os separe, pelo que devem ser o mesmo estado.
- Rever o diagrama das propostas: mistura propostas de docentes com propostas de alunos e repete a indicação de aluno pré-selecionado.
- Não juntar muitos processos no mesmo diagrama nem misturar ações de atores diferentes.

*Documentação e formatação*
- As fichas dos processos devem incluir pré-condições e resultados observáveis (pós-condições), para que o comportamento possa ser testado, incluindo o evento que provoca cada mudança de estado.
- Evitar texto bruto ou genérico que aparente ter sido gerado por IA sem revisão.
- Em vez de colar o articulado do regulamento, fazer referências diretas aos pontos do regulamento no corpo do texto e incluir a ligação oficial nas referências bibliográficas do relatório.

**Próximos passos**

1. Reformular o documento de processos aplicando todas as correções indicadas e rever a lista de processos (incluindo a retirada do P-03.1).
2. Gerar os diagramas de *state machine* em Mermaid para propostas e candidaturas.
3. Derivar os processos para **casos de uso** e **user stories** em modelo ágil (atores, pré-condições, pós-condições e critérios de aceitação), a partir da descrição detalhada dos processos.
4. Enviar ao orientador apenas o link do último *commit* do repositório com os registos de reunião.

**Decisões**

- Retirar o processo de formação de grupo (P-03.1).
- Na candidatura em grupo, o segundo elemento confirma cada uma das candidaturas do grupo, aceitando-a ou recusando-a.
- Avançar para os casos de uso e as user stories a partir da descrição detalhada dos processos.
- Inquérito com ramificação por perfil (cada perfil responde apenas aos blocos que lhe dizem respeito).
