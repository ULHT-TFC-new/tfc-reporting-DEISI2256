# Mockups estáticos (DEISI2256)

Ecrãs principais da plataforma de TFC em HTML e CSS estáticos, pedidos pelo orientador na Reunião 8 (18/11). Os dados são fictícios (baseados nos dados de demonstração do backend) e os botões não gravam nada.

**Como abrir:** abrir `index.html` no browser, ou, no Codespaces, correr `python3 -m http.server 8080` nesta pasta e abrir a porta 8080.

**Proposta → Tema → TFC:** uma proposta é o que alguém submete; depois de aceite e publicada passa a tema, a que os alunos se candidatam; quando é atribuída passa a TFC. O estado mostra sempre a fase.

| Perfil | Ecrãs |
|---|---|
| Aluno | Lista de temas com filtros; página do tema com a candidatura individual ou com um colega; candidaturas por ordem de preferência, com o colega de cada uma e os propostas dos colegas na mesma lista, com uma etiqueta azul; as minhas propostas (temass propostos pelo aluno) |
| Docente | As minhas propostas, em todas as fases e com o número de candidatos; selecionar candidato; submeter proposta |
| Coordenação | Temas e atribuições; selecionar, confirmar e publicar a atribuição (botão à parte do de selecionar) |

**CSS:** `css/mockups.css` começa com as variáveis de formatação (tipo e tamanho de letra, cores, espaços). O botão «Modo escuro» só redefine as variáveis de cor. Todas as combinações de cor têm contraste de pelo menos 4,5:1, nos dois temas, e as páginas foram verificadas com o axe-core (regras WCAG 2 A e AA) sem erros.

Os ecrãs das avaliações (por docente e de controlo) ficam para uma fase seguinte.
