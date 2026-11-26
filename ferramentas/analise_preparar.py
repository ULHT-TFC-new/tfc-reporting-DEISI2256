"""Prepara as respostas do inquérito (exportação do Microsoft Forms para Excel) para a análise.

Uso: python analise_preparar.py respostas.xlsx respostas.pkl
Identifica o perfil de cada resposta e converte as respostas de escala (\"4 - ...\") para números de 1 a 5.
"""
import pandas as pd, re, sys
df=pd.read_excel(sys.argv[1])
c=list(df.columns)
P={'Sou aluno e estou a iniciar o TFC este ano letivo (2026/2027)':'A iniciar',
   'Sou aluno e já realizei o TFC (ou já fiz entregas e avaliações de TFC)':'Ex-aluno',
   'Sou docente (orientador, jurado ou proponente de TFC)':'Docente'}
df['perfil']=df[c[6]].map(P)
def lik(v):
    if pd.isna(v): return None
    m=re.match(r'\s*(\d)',str(v))
    return int(m.group(1)) if m else None
L={8:'proposta',11:'acompanhar',12:'form_aval',17:'sabia_etapa',19:'entrega_clara',21:'verif_auto',22:'result_claros',24:'presencas_util',
   25:'encontrar',27:'info_suf',29:'ordem',32:'perceber',34:'menus',38:'satisf'}
for i,k in L.items(): df[k]=df[c[i]].map(lik)
df.to_pickle(sys.argv[2])
