"""Diagramas de classes UML (Mermaid) por área e global, a partir de uma só definição."""
import json, sys
A = "<<associação>>"
AREAS = {
"3.1": dict(
 classes={
  "AnoLetivo": ["designacao : String", "data_referencia_elegibilidade : Date", "ects_minimos : Integer", "min_candidaturas : Integer",
                "max_candidaturas : Integer", "max_orientacoes_sugeridas : Integer", "antecedencia_relatorio_dias : Integer",
                "estado : EstadoAnoLetivo", "data_fecho : DateTime [0..1]"],
  "Fase": ["tipo : TipoFase", "data_inicio : DateTime", "data_fim : DateTime"],
  "Curso": ["codigo : String", "nome : String", "ativo : Boolean"],
  "GrupoCursos": ["nome : String", "ativo : Boolean"],
  "UnidadeCurricular": ["codigo : String", "nome : String"],
  "Utilizador": ["username : String", "email : String", "nome : String", "ativo : Boolean"],
  "Aluno": ["numero : String"],
  "AlunoUC": [A, "estado : EstadoUC", "nota : Decimal [0..1]"],
  "InscricaoTFC": [A, "ects : Integer", "elegivel : Boolean"],
  "Docente": ["departamento : String", "ativo : Boolean"],
  "EntidadeExterna": ["nome : String", "tipo : TipoEntidade", "contacto : String"]},
 enums={"EstadoAnoLetivo": ["ABERTO", "FECHADO"],
        "TipoFase": ["PROPOSTAS_DOCENTES", "PROPOSTAS_EXTERNAS", "PROPOSTAS_ALUNOS", "VALIDACAO_PROPOSTAS_ALUNOS", "CANDIDATURAS", "LISTA_FINAL"],
        "EstadoUC": ["CONCLUIDA", "EM_CURSO"], "TipoEntidade": ["EMPRESA", "DEPARTAMENTO"]},
 rel=['AnoLetivo "1" *-- "1..*" Fase : tem', 'GrupoCursos "0..*" -- "1..*" Curso : agrupa',
      'Utilizador "1" -- "0..1" Aluno : é', 'Utilizador "1" -- "0..1" Docente : é',
      'Utilizador "0..*" -- "0..1" EntidadeExterna : representa', 'Curso "1" -- "0..*" Aluno : frequentado por',
      'Aluno "1" -- "0..*" AlunoUC', 'UnidadeCurricular "1" -- "0..*" AlunoUC',
      'Aluno "1" -- "0..*" InscricaoTFC', 'AnoLetivo "1" -- "0..*" InscricaoTFC']),
"3.2": dict(
 classes={
  "Proposta": ["codigo : String [0..1]", "titulo : String", "descricao : String", "area_aplicacao : String", "modalidade : Modalidade",
               "estado : EstadoProposta", "tipo_proponente : TipoProponente", "notas_internas : String", "data_submissao : DateTime",
               "data_publicacao : DateTime [0..1]"],
  "Tecnologia": ["nome : String"],
  "PropostaUC": [A, "tipo : TipoLigacaoUC"],
  "AnexoProposta": ["caminho_ficheiro : String", "nome_original : String"]},
 enums={"Modalidade": ["INDIVIDUAL", "GRUPO", "INDIVIDUAL_OU_GRUPO"],
        "EstadoProposta": ["EM_VALIDACAO", "ALTERACOES_SOLICITADAS", "ACEITE", "RECUSADA", "DISPONIVEL", "PRE_ATRIBUIDA", "ATRIBUIDA", "ARQUIVADA"],
        "TipoProponente": ["DOCENTE", "ALUNO", "EMPRESA", "DEPARTAMENTO"],
        "TipoLigacaoUC": ["REQUISITO_CONCLUIDA", "REQUISITO_EM_CURSO", "ASSOCIADA"]},
 rel=['AnoLetivo "1" -- "0..*" Proposta : tem', 'Utilizador "1" -- "0..*" Proposta : propõe',
      'EntidadeExterna "0..1" -- "0..*" Proposta : apresenta', 'Docente "0..1" -- "0..*" Proposta : orientador sugerido',
      'Utilizador "0..1" -- "0..*" Proposta : coorientador sugerido', 'Proposta "0..1" -- "0..*" Proposta : continuação de',
      'Proposta "0..*" -- "1..*" Curso : destina-se a', 'Proposta "0..*" -- "0..*" Tecnologia : usa',
      'Proposta "0..*" -- "0..2" Aluno : indica', 'Proposta "1" -- "0..*" PropostaUC', 'UnidadeCurricular "1" -- "0..*" PropostaUC',
      'Proposta "1" *-- "0..*" AnexoProposta : tem']),
"3.3": dict(
 classes={
  "Grupo": ["origem : OrigemGrupo", "estado : EstadoGrupo", "aceite_submissor : Boolean", "aceite_colega : Boolean", "data_criacao : DateTime"],
  "Candidatura": ["prioridade : Integer [0..1]", "estado : EstadoCandidatura", "motivo_fim : MotivoFim [0..1]", "data_submissao : DateTime",
                  "data_estado : DateTime"],
  "Selecao": ["posicao : Integer [0..1]", "pontuacao : Decimal [0..1]", "selecionada : Boolean", "data_selecao : DateTime [0..1]",
              "justificacao_ajuste : String", "confirmada : Boolean", "data_confirmacao : DateTime [0..1]"]},
 enums={"OrigemGrupo": ["CANDIDATURA", "JUNCAO"], "EstadoGrupo": ["PENDENTE", "ATIVO", "RECUSADO", "DISSOLVIDO"],
        "EstadoCandidatura": ["PENDENTE_CONFIRMACAO", "ATIVA", "RECUSADA", "CONTEMPLADA", "ENCERRADA", "CANCELADA"],
        "MotivoFim": ["SEM_CREDITOS", "TFC_ATRIBUIDO_A_OUTRO", "ALUNO_CONTEMPLADO", "RECUSADA_PELO_COLEGA", "SEM_CONFIRMACAO",
                      "DESISTENCIA", "CANCELADA_PELO_ALUNO", "SUBSTITUIDA"]},
 rel=['AnoLetivo "1" -- "0..*" Grupo : tem', 'Aluno "1" -- "0..*" Grupo : submissor', 'Aluno "0..1" -- "0..*" Grupo : colega',
      'Docente "0..1" -- "0..*" Grupo : propõe junção', 'Utilizador "0..1" -- "0..*" Grupo : valida',
      'Grupo "1" -- "0..*" Candidatura : candidata-se', 'Proposta "1" -- "0..*" Candidatura : recebe',
      'Candidatura "0..1" -- "0..1" Candidatura : substitui', 'Candidatura "1" -- "0..1" Selecao : selecionada em',
      'Utilizador "0..1" -- "0..*" Selecao : seleciona', 'Utilizador "0..1" -- "0..*" Selecao : confirma']),
"3.4": dict(
 classes={
  "TFC": ["estado : EstadoTFC", "repositorio_url : String", "data_atribuicao : DateTime", "epoca_final : Integer"],
  "TFCAluno": [A, "ativo : Boolean", "data_entrada : Date", "data_saida : Date [0..1]", "motivo_saida : String"],
  "Pedido": ["tipo : TipoPedido", "motivo : String", "parecer_orientador : String", "estado : EstadoPedido", "data_pedido : DateTime",
             "data_decisao : DateTime [0..1]"],
  "Atividade": ["tipo : TipoAtividade", "data : Date", "descricao : String"],
  "Entrega": ["relatorio_caminho : String", "relatorio_data_envio : DateTime [0..1]", "estado_relatorio : EstadoRelatorio [0..1]",
              "comentario_orientador : String", "data_validacao : DateTime [0..1]", "link_repositorio : String", "commit_hash : String",
              "link_video : String", "link_versao_operacional : String", "texto_divulgacao : String", "imagem_caminho : String",
              "estado : EstadoEntrega", "data_submissao : DateTime [0..1]"],
  "VerificacaoAutomatica": ["resultado : ResultadoVerificacao", "detalhes : String", "data : DateTime"]},
 enums={"EstadoTFC": ["EM_CURSO", "ADIADO", "ENTREGUE", "AVALIADO", "CONCLUIDO", "CANCELADO", "ARQUIVADO"],
        "TipoPedido": ["DESISTENCIA", "DESATRIBUICAO", "ADIAMENTO", "DISSOCIACAO"], "EstadoPedido": ["PENDENTE", "VALIDADO", "REJEITADO"],
        "TipoAtividade": ["REUNIAO", "ATIVIDADE"], "EstadoRelatorio": ["ENVIADO", "ACEITE", "DEVOLVIDO"],
        "EstadoEntrega": ["POR_SUBMETER", "SUBMETIDA", "EM_FALTA"], "ResultadoVerificacao": ["CUMPRE", "NAO_CUMPRE", "ERRO"]},
 rel=['Proposta "1" -- "0..1" TFC : dá origem a', 'Docente "1" -- "0..*" TFC : orienta', 'Utilizador "0..1" -- "0..*" TFC : coorienta',
      'TFC "1" -- "1..2" TFCAluno', 'Aluno "1" -- "0..*" TFCAluno', 'Candidatura "0..1" -- "0..1" TFCAluno : contemplada',
      'TFC "1" -- "0..*" Pedido : tem', 'Aluno "0..1" -- "0..*" Pedido : relativo a', 'Utilizador "1" -- "0..*" Pedido : pede',
      'Utilizador "0..1" -- "0..*" Pedido : valida', 'TFC "1" -- "0..*" Atividade : tem', 'Utilizador "1" -- "0..*" Atividade : regista',
      'TFC "1" -- "0..*" Entrega : faz', 'MomentoAvaliacao "1" -- "0..*" Entrega : recebe', 'Docente "0..1" -- "0..*" Entrega : valida relatório',
      'Aluno "0..1" -- "0..*" Entrega : submete', 'Entrega "1" *-- "0..*" VerificacaoAutomatica : tem']),
"3.5": dict(
 classes={
  "ModeloAvaliacao": ["versao : Integer", "niveis_escala : Integer", "limiar_discrepancia : Integer", "majoracao_orientador : Decimal",
                      "ativo : Boolean", "data_criacao : DateTime"],
  "MomentoAvaliacao": ["nome : String", "tipo : TipoMomento", "mecanismo : Mecanismo", "com_nota : Boolean", "peso : Decimal",
                       "epoca : Integer [0..1]", "requer_entrega : Boolean", "prazo_entrega : DateTime [0..1]", "prazo_avaliacao : DateTime [0..1]",
                       "data_publicacao : Date [0..1]", "ordem : Integer"],
  "Criterio": ["nome : String", "descricao : String", "peso : Decimal", "ordem : Integer"],
  "MembroJuri": [A],
  "Defesa": ["data_hora : DateTime", "local : String", "publicada_em : DateTime [0..1]"],
  "Avaliacao": ["estado : EstadoAvaliacao", "apreciacao : String", "data_criacao : DateTime", "data_submissao : DateTime [0..1]",
                "data_alteracao : DateTime"],
  "ClassificacaoCriterio": [A, "nivel : Integer", "justificacao_discrepancia : String"],
  "Seminario": ["titulo : String", "data : Date"],
  "Presenca": [A, "presente : Boolean"],
  "NotaMomento": [A, "valor : Decimal", "origem : OrigemNota", "estado : EstadoNota", "data_publicacao : DateTime [0..1]"],
  "ResultadoFinal": ["epoca : Integer", "nota_final : Integer", "situacao : Situacao", "percentagem_presencas : Decimal [0..1]",
                     "estado : EstadoNota", "data_publicacao : DateTime [0..1]"]},
 enums={"TipoMomento": ["INTERCALAR", "FINAL", "DEISIFEST", "PRESENCAS", "OUTRO"], "Mecanismo": ["JURI_CRITERIOS", "VOTACAO", "PRESENCA"],
        "EstadoAvaliacao": ["RASCUNHO", "SUBMETIDA"], "OrigemNota": ["CALCULADA", "VOTACAO", "MANUAL"],
        "EstadoNota": ["CALCULADA", "CONFIRMADA", "PUBLICADA"], "Situacao": ["APROVADO", "REPROVADO", "EXCLUIDO"]},
 rel=['AnoLetivo "1" -- "1..*" ModeloAvaliacao : tem', 'ModeloAvaliacao "1" *-- "1..*" MomentoAvaliacao : tem',
      'MomentoAvaliacao "0..1" -- "0..*" MomentoAvaliacao : conta para', 'MomentoAvaliacao "1" *-- "0..*" Criterio : tem',
      'TFC "1" -- "0..*" MembroJuri', 'MomentoAvaliacao "1" -- "0..*" MembroJuri', 'Docente "1" -- "0..*" MembroJuri',
      'TFC "1" -- "0..*" Defesa : tem', 'MomentoAvaliacao "1" -- "0..*" Defesa : em', 'Entrega "1" -- "0..*" Avaliacao : avaliada em',
      'Docente "1" -- "0..*" Avaliacao : jurado', 'Avaliacao "1" *-- "1..*" ClassificacaoCriterio', 'Criterio "1" -- "0..*" ClassificacaoCriterio',
      'MomentoAvaliacao "1" *-- "0..*" Seminario : tem', 'Seminario "1" -- "0..*" Presenca', 'Aluno "1" -- "0..*" Presenca',
      'Utilizador "0..1" -- "0..*" Presenca : regista', 'TFCAluno "1" -- "0..*" NotaMomento', 'MomentoAvaliacao "1" -- "0..*" NotaMomento',
      'Utilizador "0..1" -- "0..*" NotaMomento : confirma', 'TFCAluno "1" -- "0..*" ResultadoFinal : tem']),
"3.6": dict(
 classes={"Notificacao": ["tipo : String", "mensagem : String", "ligacao : String", "lida : Boolean", "email_enviado : Boolean", "data : DateTime"],
          "Historico": ["entidade : String", "entidade_id : Integer", "evento : String", "campo : String", "valor_anterior : String",
                        "valor_novo : String", "data : DateTime", "motivo : String"]},
 enums={},
 rel=['Utilizador "1" -- "0..*" Notificacao : recebe', 'Utilizador "0..1" -- "0..*" Historico : autor']),
}

def nome_classe(r):  # as duas classes de uma ligação
    p = r.split('"'); return p[0].strip(), p[4].split(":")[0].replace("*--", "").replace("--", "").strip()

def area(k):
    a = AREAS[k]; linhas = ["classDiagram"]
    for c, attrs in a["classes"].items():
        linhas.append(f"    class {c} {{")
        linhas += [f"        {x}" for x in attrs]
        linhas.append("    }")
    for e, vals in a["enums"].items():
        linhas.append(f"    class {e} {{\n        <<enumeration>>")
        linhas += [f"        {v}" for v in vals]
        linhas.append("    }")
    externas = sorted({c for r in a["rel"] for c in nome_classe(r)} - set(a["classes"]))
    linhas += [f"    class {c}" for c in externas]
    linhas += [f"    {r}" for r in a["rel"]]
    return "\n".join(linhas) + "\n"

def globais():
    linhas = ["classDiagram"]
    for k, a in AREAS.items():
        for c, attrs in a["classes"].items():
            linhas.append(f"    class {c}" + (f" {{\n        {A}\n    }}" if A in attrs else ""))
    vistos = []
    for a in AREAS.values():
        for r in a["rel"]:
            if r not in vistos: vistos.append(r)
    linhas += [f"    {r}" for r in vistos]
    return "\n".join(linhas) + "\n", len(vistos)

out = sys.argv[1]
for k in AREAS: open(f"{out}/classes_{k}.mmd", "w").write(area(k))
g, n = globais(); open(f"{out}/classes_global.mmd", "w").write(g)
print("classes:", sum(len(a["classes"]) for a in AREAS.values()), "associações:", n)
