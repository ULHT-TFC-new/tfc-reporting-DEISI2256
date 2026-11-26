"""Extrai o esquema do PostgreSQL (tabelas das apps da plataforma) para JSON."""
import json, sys, psycopg
APPS = ("configuracao_", "propostas_", "candidaturas_", "tfc_", "avaliacao_", "comum_")
con = psycopg.connect(host=sys.argv[1], port=sys.argv[2], user="tfc", dbname="tfc")
q = lambda sql, *a: con.execute(sql, a).fetchall()
tabelas = [t for (t,) in q("select table_name from information_schema.tables where table_schema='public' and table_type='BASE TABLE' order by 1") if t.startswith(APPS)]
out = {}
for t in tabelas:
    cols = q("""select column_name, data_type, character_maximum_length, numeric_precision, numeric_scale, is_nullable, column_default
                from information_schema.columns where table_schema='public' and table_name=%s order by ordinal_position""", t)
    cons = q("""select c.conname, c.contype, pg_get_constraintdef(c.oid),
                       array(select a.attname from unnest(c.conkey) k join pg_attribute a on a.attrelid=c.conrelid and a.attnum=k),
                       (select relname from pg_class where oid=c.confrelid)
                from pg_constraint c join pg_class r on r.oid=c.conrelid where r.relname=%s order by 1""", t)
    idx = q("""select indexname, indexdef from pg_indexes where tablename=%s and indexdef like 'CREATE UNIQUE%%' and indexdef like '%% WHERE %%'""", t)
    out[t] = {"cols": cols, "cons": cons, "partial_unique": idx}
json.dump(out, open(sys.argv[3], "w"), default=str, indent=1, ensure_ascii=False)
print(len(out), "tabelas")
