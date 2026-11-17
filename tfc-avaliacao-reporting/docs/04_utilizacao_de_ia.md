# 04 — Utilização de IA generativa

Este documento descreve como foi usada a IA generativa no TFC DEISI2257. Serve de base à nota prévia dos anexos do relatório e ao inquérito sobre IA generativa pedido no regulamento (anexo E).

## 1. Ferramenta

- **Ferramenta:** Claude, da Anthropic, através da aplicação claude.ai.
- **Período:** desde o início do TFC (setembro de 2026) e ao longo de todo o trabalho.

## 2. Princípios seguidos

- As decisões do trabalho são do aluno, da equipa e do orientador: regras da plataforma, divisão do trabalho, tecnologias e arquitetura. A IA foi usada para organizar, redigir, propor alternativas e escrever código a partir dessas decisões.
- A informação de base veio sempre de fontes identificadas: o regulamento de TFC, as reuniões e os emails do orientador, as respostas ao inquérito e o trabalho dos colegas dos outros TFC.
- Todo o resultado foi revisto pelo aluno antes de entrar no repositório ou de ser enviado ao orientador.
- Os documentos feitos com apoio de IA têm um aviso no início, com ligação para este documento.

## 3. Utilização por artefacto

| Artefacto | O que a IA fez | O que fez o aluno |
|---|---|---|
| [Registo do projeto](reunioes.md) | Organizou as notas das reuniões a partir das notas e das gravações das reuniões; manteve o planeamento e o registo de atividades | Forneceu as notas e as gravações, corrigiu e cortou o que não estava certo ou não era relevante, e enviou o registo ao orientador |
| [Inquérito](01_inquerito.md) | Propôs a estrutura, a ramificação por perfil e a redação das perguntas a partir do primeiro rascunho do aluno; aplicou as alterações pedidas pelo orientador | Fez o primeiro rascunho, criou o formulário no Microsoft Forms, testou os percursos, publicou e acompanhou as respostas |
| [Lista de processos](02_processos.md) | Corrigiu e reorganizou a lista de processos feita pelo colega; redigiu as fichas detalhadas, as máquinas de estados e os diagramas; aplicou as indicações das reuniões e as respostas do orientador | Comparou com a versão do colega, levou as questões em aberto ao orientador, tomou as decisões que cabiam à equipa (por exemplo, a confirmação de cada candidatura do grupo) e reviu o documento |
| [Análise exploratória](analise-exploratoria.md) | Tratou os dados exportados do Forms em Python, calculou as distribuições, fez os gráficos e agrupou as respostas abertas por tema; ajustou a análise às indicações do orientador | Recolheu os dados, reviu os resultados e a agrupação das respostas abertas |
| [Modelo de dados](03_modelo_de_dados.md) | Propôs as classes, os atributos, as regras na base de dados e as vistas a partir da lista de processos | Definiu as prioridades, reviu o modelo e as questões em aberto |
| Backend (pasta `backend/`) | Escreveu o código inicial em Django: modelos, migrações, regras em PL/pgSQL, API, testes automáticos e configuração do Docker | Escolheu a linguagem e a framework (Python com Django) depois de estudar as alternativas, testou, integrou no repositório e mantém o código |

## 4. Verificação

- **Código:** o comportamento das regras da base de dados é verificado por testes automáticos (`python manage.py test`).
- **Diagramas:** os diagramas Mermaid foram gerados e verificados antes de entrarem nos documentos.
- **Análise:** os números da análise foram calculados por código a partir dos dados exportados, e não estimados.
- **Regulamento:** as referências ao regulamento são confirmadas pelo aluno no documento original.
