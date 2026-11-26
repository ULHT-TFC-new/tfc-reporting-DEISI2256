# Ferramentas

Scripts usados para gerar partes da documentação. Permitem voltar a gerar os diagramas e os gráficos quando o código ou os dados mudam, em vez de os editar à mão.

| Script | O que gera | Uso |
|---|---|---|
| `extrair_esquema.py` | Lê do PostgreSQL as tabelas, colunas, chaves e restrições da plataforma e grava-as em JSON | `python extrair_esquema.py <host> <porta> esquema.json` |
| `gerar_er.py` | Diagrama E-R completo (Mermaid `erDiagram`) e tabela de restrições da secção 2.2 de `docs/03_modelo_de_dados.md` | `python gerar_er.py esquema.json er.mmd restricoes.md` |
| `gerar_classes.py` | Diagramas de classes UML (Mermaid `classDiagram`) por área e global, das secções 2.1 e 3 | `python gerar_classes.py <pasta de saída>` |
| `analise_preparar.py` | Prepara as respostas do inquérito exportadas do Microsoft Forms | `python analise_preparar.py respostas.xlsx respostas.pkl` |
| `analise_graficos.py` | Os 5 gráficos de `docs/img/analise/` | `python analise_graficos.py respostas.pkl ../docs/img/analise` |

O E-R é gerado a partir da base de dados depois de aplicadas todas as migrações (`python manage.py migrate`), por isso coincide sempre com o código. Os diagramas de classes são definidos em `gerar_classes.py`: quando o modelo muda, altera-se esse ficheiro e voltam a gerar-se os diagramas.

O ficheiro Excel com as respostas do inquérito não está no repositório.

Requisitos: Python 3.13, `psycopg` (E-R), `pandas`, `openpyxl` e `matplotlib` (análise).
