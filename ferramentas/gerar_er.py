"""Gera o diagrama E-R (Mermaid erDiagram) e a tabela de restrições a partir do esquema extraído."""
import json, re, sys
d = json.load(open(sys.argv[1]))
NOMES = {
 "configuracao_anoletivo":"ANO_LETIVO","configuracao_fase":"FASE","configuracao_curso":"CURSO",
 "configuracao_grupocursos":"GRUPO_CURSOS","configuracao_grupocursos_cursos":"GRUPO_CURSOS_CURSO",
 "configuracao_unidadecurricular":"UNIDADE_CURRICULAR","configuracao_entidadeexterna":"ENTIDADE_EXTERNA",
 "configuracao_utilizador":"UTILIZADOR","configuracao_aluno":"ALUNO","configuracao_alunouc":"ALUNO_UC",
 "configuracao_inscricaotfc":"INSCRICAO_TFC","configuracao_docente":"DOCENTE",
 "propostas_tecnologia":"TECNOLOGIA","propostas_proposta":"PROPOSTA","propostas_proposta_cursos":"PROPOSTA_CURSO",
 "propostas_proposta_tecnologias":"PROPOSTA_TECNOLOGIA","propostas_propostauc":"PROPOSTA_UC",
 "propostas_propostaaluno":"PROPOSTA_ALUNO","propostas_anexoproposta":"ANEXO_PROPOSTA",
 "candidaturas_grupo":"GRUPO","candidaturas_candidatura":"CANDIDATURA","candidaturas_selecao":"SELECAO",
 "tfc_tfc":"TFC","tfc_tfcaluno":"TFC_ALUNO","tfc_pedido":"PEDIDO","tfc_atividade":"ATIVIDADE","tfc_entrega":"ENTREGA",
 "tfc_verificacaoautomatica":"VERIFICACAO_AUTOMATICA",
 "avaliacao_modeloavaliacao":"MODELO_AVALIACAO","avaliacao_momentoavaliacao":"MOMENTO_AVALIACAO",
 "avaliacao_criterio":"CRITERIO","avaliacao_membrojuri":"MEMBRO_JURI","avaliacao_defesa":"DEFESA",
 "avaliacao_avaliacao":"AVALIACAO","avaliacao_classificacaocriterio":"CLASSIFICACAO_CRITERIO",
 "avaliacao_seminario":"SEMINARIO","avaliacao_presenca":"PRESENCA","avaliacao_notamomento":"NOTA_MOMENTO",
 "avaliacao_resultadofinal":"RESULTADO_FINAL","comum_notificacao":"NOTIFICACAO","comum_historico":"HISTORICO",
}
# Colunas herdadas do utilizador do Django que não interessam ao modelo
OMITIR = {"configuracao_utilizador": {"first_name", "last_name", "is_staff", "is_superuser", "date_joined"}}

def tipo(c):
    # NUMERIC sem (p,s): a vírgula dentro do tipo não é aceite pelo Mermaid usado no GitHub
    _, t, n, p, s, *_ = c
    return {"bigint":"BIGINT","smallint":"SMALLINT","integer":"INTEGER","text":"TEXT","boolean":"BOOL",
            "date":"DATE","jsonb":"JSONB","timestamp with time zone":"TIMESTAMPTZ"}.get(t) or \
           (f"VARCHAR({n})" if t=="character varying" else "NUMERIC" if t=="numeric" else t.upper())

linhas, rels, restricoes = ["erDiagram"], [], []
for t in NOMES:
    info = d[t]
    E = NOMES[t]
    pk = {c for name, ty, _, cols, _ in info["cons"] if ty=="p" for c in cols}
    fk = {cols[0]: ref for name, ty, _, cols, ref in info["cons"] if ty=="f"}
    uk1 = {cols[0] for name, ty, _, cols, _ in info["cons"] if ty=="u" and len(cols)==1}
    linhas.append(f"    {E} {{")
    for c in info["cols"]:
        if c[0] in OMITIR.get(t, ()): continue
        chaves = ",".join(k for k, ok in (("PK", c[0] in pk), ("FK", c[0] in fk), ("UK", c[0] in uk1)) if ok)
        nn = "NN" if c[5]=="NO" else "NULL"
        linhas.append(f"        {c[0]} {tipo(c)}" + (f" {chaves}" if chaves else "") + f' "{nn}"')
    linhas.append("    }")
    nulos = {c[0]: c[5]=="YES" for c in info["cols"]}
    for col, ref in fk.items():
        if ref not in NOMES: continue
        pai = "|o" if nulos[col] else "||"
        filho = "o|" if col in uk1 else "o{"
        rels.append(f'    {NOMES[ref]} {pai}--{filho} {E} : "{col.removesuffix("_id")}"')
    for name, ty, defn, cols, _ in info["cons"]:
        if ty == "c" and not re.fullmatch(r"CHECK \(\(\w+ >= 0\)\)", defn):   # os >= 0 dos inteiros positivos são automáticos
            restricoes.append((E, "CHECK", name, defn.removeprefix("CHECK ")))
        if ty == "u" and len(cols) > 1:
            restricoes.append((E, "UNIQUE", name, "(" + ", ".join(cols) + ")"))
    for name, defn in info["partial_unique"]:
        m = re.search(r"\((.*?)\) WHERE (.*)$", defn)
        cond = re.sub(r"::(text|character varying)(\[\])?", "", m.group(2)).replace("ARRAY[", "[")
        restricoes.append((E, "UNIQUE parcial", name, f"({m.group(1)}) WHERE {cond}"))
open(sys.argv[2], "w").write("\n".join(linhas + rels) + "\n")
with open(sys.argv[3], "w") as f:
    f.write("| Entidade | Tipo | Nome | Definição |\n|---|---|---|---|\n")
    for r in sorted(restricoes):
        f.write("| " + " | ".join(r[:3]) + " | `" + r[3].replace("|", "\\|") + "` |\n")
print(sum(1 for l in linhas if l.endswith("{")), "entidades,", len(rels), "relações,", len(restricoes), "restrições")
