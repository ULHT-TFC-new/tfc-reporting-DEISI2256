# DEISI2257 — Modernização da Plataforma de Gestão de TFC: Avaliação e Reporting

Trabalho Final de Curso (TFC), Departamento de Engenharia Informática e Sistemas de Informação (DEISI), Universidade Lusófona, ano letivo 2026/27.

| | |
|---|---|
| **Aluno** | Tomás Cruz |
| **Orientador** | Prof. Luís Gomes |
| **Entidade** | ULHT-DEISI |

## Contexto

A plataforma de gestão de TFC do DEISI tem sido essencial ao longo dos últimos anos, mas tem revelado lacunas decorrentes da evolução tecnológica e do crescimento dos cursos. Este TFC faz parte de um conjunto de três projetos que, em conjunto, modernizam a plataforma:

| TFC | Âmbito |
|---|---|
| DEISI2256 | Frontend de toda a plataforma |
| **DEISI2257** | **Backend de toda a plataforma (lógica de negócio, API e base de dados), com foco na avaliação e no reporting** (este repositório) |
| DEISI2258 | Verificação automática dos entregáveis no GitHub |

Os três projetos partilham a mesma base de dados, mantendo resultados distintos e autónomos, conforme exigido pelo regulamento de TFC.

## Objetivos

- Incorporar na plataforma ferramentas de reporting para os vários perfis de utilizador (coordenação, docentes e alunos).
- Criar mecanismos para flexibilizar a configuração das avaliações (momentos, critérios e pesos), incluindo o apuramento de resultados.
- Integrar na base de dados os dados relativos à avaliação.

## Documentação

| Documento | Conteúdo |
|---|---|
| [Registo do projeto](docs/reunioes.md) | Planeamento, registo de atividades e notas das reuniões |
| [01 — Inquérito](docs/01_inquerito.md) | Inquérito aos utilizadores da plataforma atual |
| [Análise exploratória](docs/analise-exploratoria.md) | Análise das respostas ao inquérito |
| [02 — Processos](docs/02_processos.md) | Macro-processos, processos e máquinas de estados da plataforma |
| [03 — Modelo de dados](docs/03_modelo_de_dados.md) | Diagrama de classes, regras na base de dados e vistas de reporting |
| [04 — Utilização de IA](docs/04_utilizacao_de_ia.md) | Como foi usada a IA generativa no trabalho |

## Arquitetura

| Contentor | Tecnologia | Responsável |
|---|---|---|
| Base de dados | PostgreSQL 16 | DEISI2257 |
| Backend | Python 3.13, Django 5.2, Django REST Framework | DEISI2257 |
| Frontend | A definir | DEISI2256 |

Instruções para arrancar o backend, endpoints e testes: [backend/README.md](backend/README.md).

```bash
cp .env.example .env
docker compose up --build
```

## Estado do projeto

- Inquérito concluído (60 respostas) e analisado.
- Lista de processos revista com o orientador.
- Modelo de dados definido e implementado no backend, com as primeiras regras na base de dados (lista de candidaturas e atribuição de TFC) e testes automáticos.
- Em curso: use cases e user stories, restantes regras da base de dados, vistas de reporting e relatório da 1.ª entrega (13/12/2026).
