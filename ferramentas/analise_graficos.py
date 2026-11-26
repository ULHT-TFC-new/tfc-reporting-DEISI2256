"""Gera os 5 gráficos da análise exploratória (docs/img/analise/) a partir do ficheiro preparado.

Uso: python analise_graficos.py respostas.pkl ../docs/img/analise
"""
import sys, pandas as pd, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter
df=pd.read_pickle(sys.argv[1]); out=sys.argv[2]; c=df.columns
SURF='#ffffff'; INK='#0b0b0b'; INK2='#52514e'; GRID='#e4e3df'; BLUE='#2a78d6'
LIK={1:'#e34948',2:'#f2a3a2',3:'#cfcec9',4:'#86b6ef',5:'#2a78d6'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'text.color':INK,'axes.labelcolor':INK2,
 'xtick.color':INK2,'ytick.color':INK,'axes.edgecolor':GRID,'figure.facecolor':SURF,'axes.facecolor':SURF})
def clean(ax):
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(GRID); ax.tick_params(axis='y',length=0)
def save(fig,name): fig.savefig(f'{out}/{name}',dpi=200,bbox_inches='tight',facecolor=SURF); plt.close(fig)
A=df[df.perfil=='A iniciar']; nA=len(A)

# F1 perfis
cnt=df.perfil.value_counts().reindex(['A iniciar','Docente','Ex-aluno'])
lab=['Alunos a iniciar o TFC','Docentes','Alunos que já realizaram o TFC']
fig,ax=plt.subplots(figsize=(7,2.2)); y=np.arange(3)[::-1]
ax.barh(y,cnt.values,color=BLUE,height=0.55)
for yi,v in zip(y,cnt.values): ax.text(v+0.6,yi,str(v),va='center',color=INK)
ax.set_yticks(y,lab); ax.set_xticks([]); clean(ax); ax.spines['bottom'].set_visible(False)
ax.set_title(f'Respostas por perfil (n = {len(df)})',loc='left',fontsize=11,color=INK); save(fig,'fig1_perfis.png')

# F2 Likert stacked
items=[('encontrar','Encontrar TFC do meu interesse'),('info_suf','Informação de cada TFC suficiente para decidir'),
 ('ordem','Definir e alterar a ordem de preferência'),('perceber','Perceber o que fazer a seguir ao entrar'),
 ('menus','Clareza dos nomes dos menus'),('satisf','Satisfação geral')]
fig,ax=plt.subplots(figsize=(8.5,3.6)); y=np.arange(len(items))[::-1]
for yi,(k,_) in zip(y,items):
    s=A[k].dropna(); left=0
    for lv in range(1,6):
        p=(s==lv).mean()*100
        ax.barh(yi,p,left=left,color=LIK[lv],height=0.6,edgecolor=SURF,linewidth=1.5)
        if p>=8: ax.text(left+p/2,yi,f'{p:.0f}%',ha='center',va='center',fontsize=8.5,color=INK if lv in (2,3,4) else '#ffffff')
        left+=p
    ax.text(102,yi,f'{(s>=4).mean()*100:.0f}%',va='center',fontsize=9.5,color=INK,fontweight='bold')
ax.text(102,len(items)-0.35,'4–5',fontsize=8.5,color=INK2)
ax.set_yticks(y,[t for _,t in items]); ax.set_xlim(0,108); ax.set_xticks([0,25,50,75,100],['0%','25%','50%','75%','100%']); clean(ax)
h=[plt.Rectangle((0,0),1,1,color=LIK[i]) for i in range(1,6)]
ax.legend(h,['1 (pior)','2','3','4','5 (melhor)'],ncol=5,loc='upper left',bbox_to_anchor=(0,-0.1),frameon=False,fontsize=8.5,handlelength=1,columnspacing=1.2)
ax.set_title(f'Alunos a iniciar o TFC: avaliação de 1 a 5 (n = {nA})',loc='left',fontsize=11); save(fig,'fig2_escalas_alunos.png')

def multi(sub,col):
    return Counter(x.strip() for v in sub[col].dropna() for x in str(v).split(';') if x.strip())
def hbar(counts,n,title,name,order=None):
    items=order or [k for k,_ in counts.most_common()]
    fig,ax=plt.subplots(figsize=(7,0.42*len(items)+0.8)); y=np.arange(len(items))[::-1]
    vals=[counts[k]/n*100 for k in items]
    ax.barh(y,vals,color=[BLUE if k!='Nenhum' else '#b5b4af' for k in items],height=0.6)
    for yi,k,v in zip(y,items,vals): ax.text(v+1,yi,f'{v:.0f}% ({counts[k]})',va='center',fontsize=9)
    ax.set_yticks(y,items); ax.set_xticks([]); ax.set_xlim(0,max(vals)*1.25); clean(ax); ax.spines['bottom'].set_visible(False)
    ax.set_title(title,loc='left',fontsize=11); save(fig,name)
f=multi(A,c[26]); order=[k for k,_ in f.most_common() if k!='Nenhum']+['Nenhum']
hbar(f,nA,f'Filtros em falta na lista de propostas (alunos a iniciar, n = {nA})','fig3_filtros.png',order)
hbar(multi(A,c[33]),nA,f'Informação pretendida na página inicial (alunos a iniciar, n = {nA})','fig4_pagina_inicial.png')

# F5 devices
DEV={'Muito má':1,'Má':2,'Razoável':3,'Boa':4,'Muito boa':5}
fig,ax=plt.subplots(figsize=(8.5,2.2)); y=np.arange(3)[::-1]
for yi,col in zip(y,[c[35],c[36],c[37]]):
    s=A[col]; left=0
    for lbl,lv in DEV.items():
        v=(s==lbl).sum()
        ax.barh(yi,v,left=left,color=LIK[lv],height=0.6,edgecolor=SURF,linewidth=1.5)
        if v>=3: ax.text(left+v/2,yi,str(v),ha='center',va='center',fontsize=8.5,color=INK if lv in (2,3,4) else '#ffffff')
        left+=v
    v=(s=='Não uso').sum()
    ax.barh(yi,v,left=left,color='#f3f2ef',height=0.6,edgecolor='#b5b4af',linewidth=0.8,hatch='///')
    if v>=3: ax.text(left+v/2,yi,str(v),ha='center',va='center',fontsize=8.5,color=INK2)
ax.set_yticks(y,['Computador','Telemóvel','Tablet']); ax.set_xlim(0,nA); ax.set_xticks([0,12,24,36,48]); ax.set_xlabel('número de respostas'); clean(ax)
h=[plt.Rectangle((0,0),1,1,color=LIK[i]) for i in range(1,6)]+[plt.Rectangle((0,0),1,1,facecolor='#f3f2ef',edgecolor='#b5b4af',hatch='///')]
ax.legend(h,list(DEV)+['Não uso'],ncol=6,loc='upper left',bbox_to_anchor=(0,-0.35),frameon=False,fontsize=8.5,handlelength=1,columnspacing=1.1)
ax.set_title(f'Experiência por dispositivo (alunos a iniciar, n = {nA})',loc='left',fontsize=11); save(fig,'fig5_dispositivos.png')
print('ok')
