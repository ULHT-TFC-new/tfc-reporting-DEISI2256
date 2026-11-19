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

### Reunião 7 — 11/11/2026

**Com:** Prof. Luís Gomes (orientador)

*O que foi falado*

  *1. Análise dos Inquéritos e Notas de Reunião*

- **Alunos do ano em curso:** Obtiveram-se 48 respostas num universo de cerca de 80 alunos inscritos (aproximadamente 2/3 da turma), o que tem significado estatístico e será avaliado com foco na fase de inscrições dos TFCs (onde os processos sofrerão maior alteração).
- **Alunos de anos anteriores:** As 4 respostas recolhidas (aproximadamente 5% da turma) não têm significado estatístico e não serão tratadas, devendo apenas ser colocada uma nota na análise a indicar essa limitação.
- **Docentes:** As 8 respostas obtidas (cerca de 1/3 dos professores envolvidos) não são estatisticamente relevantes para análises detalhadas ou gráficos circulares (*pie charts*), mas indicam tendências. Deve isolar-se apenas 3 a 4 perguntas com respostas unânimes ou tendências muito claras, adicionando uma nota de que o desenho da aplicação as terá em conta.

*2. Prazos, Arquitetura e Código Legado*

- O orientador lembrou que falta exatamente um mês para a entrega final do trabalho (a contar do dia 11 de novembro).
- Deve ser iniciada a escrita do relatório e a definição da estrutura do documento, bem como o desenho da arquitetura da aplicação.
- A equipa tem total liberdade para escolher a *stack* tecnológica (como Kotlin/Java ou Django/Python para o *backend*, e React para o *frontend*), devendo a IA ser usada apenas no apoio à configuração do ambiente de desenvolvimento.
- O código da aplicação existente (com cerca de 10 anos e sem evolução nos últimos 5-6 anos) será disponibilizado para testes, mas **não deve ser reaproveitado**.
- O regulamento exige uma proposta de arquitetura definida e um protótipo funcional (*wireframe*).
- A aplicação terá de integrar com a API do GitHub para chamadas a funções, ações e repositórios. Como a linguagem do *backend* afeta essa integração, a equipa deve dedicar 1 a 2 horas a pesquisar a documentação da API do GitHub antes de tomar a decisão final.

*3. Separação Frontend/Backend e Infraestrutura*

- O trabalho deve ser separado entre *frontend* e *backend*, acordando conjuntamente a componente transacional exposta pela base de dados. Regras internas (*triggers*, funções, *views*) ficam a cargo da implementação de *backend*.
- Deve decidir-se se a comunicação de leitura/escrita é feita por SQL direto no código (*pipes*) ou através de uma camada de API.
- Para a reunião seguinte, a equipa deve levar cenários de arquitetura formulados para testar o seu encaixe na infraestrutura oficial de publicação de TFCs a apresentar pelo Prof. Rui Santos.

*4. Processos, Gestão de Entregáveis e Templates de Avaliação*

- O ficheiro de processos de 9 de novembro foi revisto e validado quanto aos momentos de avaliação (tópico 6) e configuração do ano letivo (tópico 8).
- A submissão e validação de relatórios *draft* pelo orientador (processos P052 e P053) será efetuada dentro da plataforma.
- **Regra de armazenamento:** Para evitar o crescimento excessivo da base de dados, não se devem guardar ficheiros nem *drafts* na base de dados. Ao submeter um novo *draft*, deve executar-se a função `delete` para apagar o anterior. Os ficheiros devem ser mantidos no sistema de ficheiros ou no repositório do GitHub (na organização da faculdade), registando na base de dados apenas o *hash* do *commit* (`git commit SHA`).
- **Templates de avaliação (Tópico 8):** O tópico 8 deve ser reajustado para definir os 4 *templates* modelo da plataforma:
  1. Avaliação Intercalar;
  2. Avaliação Final com júri/apresentação presencial;
  3. Avaliação Final sem júri/apresentação presencial;
  4. DaisyFest (votação por pares com registo de média e presenças).

### Reunião 8 — 18/11/2026

**Com:** Prof. Luís Gomes (orientador) e o grupo DEISI2257

**O que foi falado**

*Mockups e interface (frontend)*
- O protótipo apresentado está graficamente limpo. As cores e o estilo são uma escolha da equipa e não são relevantes nesta fase.
- O esquema de navegação segue a mesma lógica dada em IHM. O mockup pode ser feito diretamente em HTML e é estático: não é preciso que os processos funcionem.
- Por volta de maio, o protótipo funcional vai ser apreciado e comentado pelos colegas; as questões de cores ajustam-se nessa altura.
- **CSS com variáveis:** definir no início da CSS as variáveis de formatação (tipo e tamanho de letra, cores, etc.), para se poder mudar o aspeto, por exemplo de fundo escuro para fundo claro, alterando só as variáveis.
- **Acessibilidade:** a formatação deve cumprir as normas de acessibilidade do W3C, pelo menos ao nível A.
- **Contraste:** os cartões dos TFC têm texto escuro sobre fundo escuro, com pouco contraste. Corrigir.

*Ecrãs a fazer agora em mockup*
- **Aluno:** lista de propostas, página do TFC com a candidatura e a parte do grupo. A candidatura em grupo é muito diferente da plataforma atual, por isso convém validá-la já com um mockup.
- **Docente:** submeter proposta e selecionar candidatos. Na lista, o docente vê quantos candidatos tem cada TFC, abre o TFC, vê os candidatos e seleciona-o na mesma página.
- **Coordenação:** usa as mesmas páginas dos docentes, mas vê todos os TFC e não só os seus.
- **Seleção e publicação:** a seleção é igual, seja feita pelo orientador, pelo proponente ou pela coordenação. O orientador ou o proponente escolhe o candidato; a coordenação tem um botão de confirmar que, na prática, é publicar, para a atribuição ficar fechada e pública. São botões diferentes.
- **Avaliações (mais tarde):** dois ecrãs, o das avaliações por docente e o de controlo das avaliações. Aqui os orientadores não se distinguem dos outros docentes.

*Arquitetura*
- A arquitetura tem de se ajustar à plataforma de publicação que vai ser apresentada pelo Prof. Rui Santos. A equipa deve ver essa apresentação e os requisitos de publicação antes de fechar a arquitetura.
- O ponto de partida são três contentores: frontend, backend e base de dados.
- A base de dados costuma ser o problema nestas plataformas, por causa dos recursos que exige. Pode ser preciso usar uma base de dados externa alojada, com acesso por API.

*Modelo de dados (apresentado pelo DEISI2257)*
- **Grupos:** guardar a informação na tabela do grupo e não na do aluno, tratando os trabalhos individuais como grupos de um. Dá menos trabalho na programação que alimenta o frontend.
- **Avaliações:** as avaliações são individuais por docente, mas não estão ligadas ao momento de avaliação. Com o modelo atual, cada docente só pode avaliar cada TFC uma vez, o que não funciona.
- **Correção:** ligar a avaliação à **entrega** e não ao TFC. Como a entrega identifica o TFC e o momento, deixa de haver duplicação e o momento fica implícito.
- O orientador perguntou o que é a tabela «fase» (fases do calendário do ano letivo).
- Aplicar também ao outro trabalho o que foi discutido para este.

*Casos de uso e histórias de utilizador*
- Os casos de uso estão bem feitos; o problema é terem as histórias de utilizador dentro.
- Uma história de utilizador **não é uma subdivisão** de um caso de uso. São complementares, mas não são a mesma coisa, por isso não devem estar no mesmo sítio nem repetir-se. Se forem iguais, escolhe-se um e deixa-se o outro.
- Os critérios de aceitação ficam no caso de uso, **antes das pós-condições**, e são **testes** (*test cases*), não critérios escritos.
- Corrigir a formatação do texto e as traduções literais (por exemplo, «Como coordenação», de *As a coordinator*).
- O orientador perguntou se havia um diagrama de casos de uso de visão geral; foram mostrados os diagramas por ator.

*Fecho*
- O orientador vai ver com mais atenção os documentos enviados e mandar o feedback.

**Próximos passos**
1. Fazer os mockups estáticos dos ecrãs principais: lista de propostas, candidatura e grupo do aluno; seleção de candidatos do docente; vista da coordenação com o botão de publicar.
2. Reorganizar a CSS com variáveis de formatação no início, rever o contraste dos cartões e cumprir pelo menos o nível A de acessibilidade.
3. Ver a apresentação do Prof. Rui Santos e ajustar a arquitetura aos requisitos de publicação, em particular a base de dados.
4. DEISI2257: ligar a avaliação à entrega e guardar a informação dos trabalhos no grupo, com os individuais como grupos de um.
5. Separar as histórias de utilizador dos casos de uso e escrever os critérios de aceitação como casos de teste, antes das pós-condições.

**Decisões**
- Os mockups desta fase são estáticos e podem ser feitos em HTML.
- As cores ficam à escolha da equipa, mas a CSS usa variáveis e cumpre as normas de acessibilidade.
- O orientador ou o proponente seleciona o candidato e a coordenação publica a atribuição.
- A avaliação passa a estar ligada à entrega.
- Os trabalhos individuais são tratados como grupos de um.
- Casos de uso e histórias de utilizador ficam em documentos separados.
