# 04 — Utilização de IA generativa (DEISI2256, Frontend)

Este documento descreve como usei a IA generativa no TFC DEISI2256. Serve de base à nota prévia dos anexos do relatório e ao inquérito sobre IA generativa pedido no regulamento (anexo E).

## 1. Ferramenta

- **Ferramenta:** Claude, da Anthropic, através da aplicação claude.ai.
- **Período:** outubro e novembro de 2026, em várias conversas:
  - outubro: documento do inquérito;
  - novembro: revisão da lista de processos, cenários de arquitetura e casos de uso;
  - 17/11: demonstração da integração entre o frontend e o backend;
  - 18/11: README do repositório e este documento.

## 2. Princípios seguidos

- As decisões do trabalho são minhas e da equipa. A arquitetura, os endpoints e o formato do JSON foram definidos pelo colega responsável pelo backend (DEISI2257). A escolha da tecnologia do backend foi da equipa (17/11) e não foi entregue à IA, como pediu o orientador na Reunião 7 (11/11).
- A IA foi usada para explicar procedimentos, escrever código a partir da API já existente, ajudar a resolver erros, rever documentos e redigir documentação.
- A informação de base veio do regulamento de TFC, das reuniões e dos emails do orientador, das respostas ao inquérito, do repositório do colega (código do backend e documentação) e do guião de arranque que ele enviou.
- Todo o código foi testado por mim antes de ser enviado para o repositório, e todos os documentos foram revistos por mim.
- Os documentos feitos com apoio de IA têm um aviso no início, com ligação para este documento.

## 3. Utilização por artefacto

| Artefacto | O que a IA fez | O que fiz eu |
|---|---|---|
| Organização do repositório | Explicou as opções para integrar o backend do colega no meu repositório (clone, fork, cópia de pasta, submódulo) e os comandos de Git. Indicou como verificar que os ficheiros sensíveis (`.env`) e a pasta `node_modules` não eram enviados. Explicou como mudar o nome da pasta do backend sem estragar o Docker | Escolhi a estrutura (`backend/` e `frontend/`), corri os comandos, verifiquei com `git check-ignore` e `git status`, mudei o nome da pasta e fiz os commits e os pushes |
| Frontend (`frontend/`) | Leu o código do backend (serializer, views e filtros de propostas) para identificar os campos reais do JSON. Escreveu o `App.jsx` e o `App.css`: página da lista de propostas com pesquisa e filtros por curso, tecnologia e orientador, que chama `/api/propostas/` e `/api/cursos/` | Criei o projeto com Vite e React, coloquei os ficheiros, testei a página com os dados de demonstração e verifiquei os filtros |
| Arranque do ambiente | Guiou-me pelos passos do guião do colega (Docker Compose, `carregar_demo`, Vite) e ajudou a diagnosticar os erros que apareceram: `index.css` em falta, `docker compose` corrido na pasta errada e comando de verificação corrido fora da raiz do repositório | Corri os comandos, resolvi os erros e confirmei que o backend e o frontend comunicavam |
| [Inquérito](01_inquerito.md) | Organizou em Markdown a estrutura do inquérito feito por um colega (secções, perguntas e ramificação) | Forneci o inquérito e a lista de processos como contexto, pedi as alterações e revi o documento |
| [Lista de processos](02_processos.md) | Propôs a reescrita das secções afetadas pelo feedback do orientador (fecho do ano letivo, consultas e notificações, candidaturas em grupo e substituição, momentos e critérios de avaliação, máquinas de estados) e comparou versões do documento | Forneci o feedback do orientador e as versões, escolhi o que integrar e revi o documento comum com o DEISI2257 |
| [Cenários de arquitetura](cenarios_arquitetura_para_validacao.md) | Comparou as bibliotecas da API do GitHub em Python e em Java/Kotlin e redigiu os três cenários, com diagramas Mermaid, e as perguntas para o Prof. Rui Santos, a partir das decisões já tomadas pela equipa e do código do repositório | Defini o contexto e as restrições, forneci o repositório e revi o documento |
| [Casos de uso](05_casos_de_uso.md) | Derivou os casos de uso e os critérios de aceitação das fichas da lista de processos, ligou-os ao modelo de dados e assinalou as lacunas encontradas; desenhou os diagramas. Depois da reunião de 18/11, tirou as histórias de utilizador dos casos de uso e pôs os critérios de aceitação antes das pós-condições. Depois do email do orientador de 23/11, redesenhou os diagramas de casos de uso em notação UML com a sintaxe `usecase-beta` do Mermaid 12 e verificou-os com o Mermaid 12.3 | Pedi o trabalho, forneci o repositório e as correções do orientador, pedi alterações aos diagramas até ficarem legíveis e revi os casos de uso |
| [README.md](README.md) | Redigiu uma primeira versão (estrutura do repositório, arquitetura, requisitos, passos de arranque, endpoints e problemas comuns) e, depois, uma nova versão com o projeto, o estado, a documentação e um índice | Revi o conteúdo, copiei-o para a raiz do repositório e fiz o commit |

O backend, o modelo de dados e a análise exploratória foram feitos no DEISI2257; a utilização de IA nesses artefactos está descrita no documento do DEISI2257 (`backend/docs/04_utilizacao_de_ia.md`).

## 4. Verificação

- **Código do frontend:** testei a página no browser contra o backend a correr em Docker, com os dados de demonstração. Confirmei que a lista mostra 4 propostas e que os filtros devolvem os resultados esperados (por exemplo, o curso LIG com a tecnologia React devolve a proposta DEMO04).
- **Dados da API:** comparei o JSON de `localhost:8000/api/propostas/` com o que a página mostra.
- **Segurança:** confirmei antes do commit que o `.env` do backend e a pasta `node_modules` estavam ignorados pelo Git.
- **Mudança de nome da pasta:** voltei a arrancar o backend, a carregar os dados de demonstração e a testar a página depois de mudar o nome.
- **Documentos:** cada caso de uso tem o mesmo número do processo de que deriva (`UC-xx.yy` e `P-xx.yy`) e foi confrontado com a ficha do processo, com o modelo de dados e com o código do backend. Os diagramas Mermaid foram verificados com o parser do Mermaid e renderizados antes de entrarem nos documentos.
- **Regulamento e bibliotecas:** as referências ao regulamento são confirmadas no documento original, e as versões e os limites da API do GitHub na documentação oficial.
- **Limitações:** a IA não executou o código do frontend nem o backend; toda a execução e os testes foram feitos por mim. O `README.md` descreve os passos que segui, mas não foi testado de raiz num computador diferente.
