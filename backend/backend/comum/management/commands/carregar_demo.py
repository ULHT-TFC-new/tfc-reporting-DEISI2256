"""Carrega dados de demonstração num ano letivo próprio ("DEMO"), com a fase de candidaturas aberta.

Uso: python manage.py carregar_demo
Cria docentes, alunos, propostas e candidaturas e atribui um TFC com a função atribuir_tfc,
para se ver as regras da base de dados a funcionar. Pode ser corrido várias vezes: apaga e recria o ano DEMO.
"""
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import connection, transaction
from django.utils import timezone

from candidaturas.models import Candidatura
from comum.models import Historico
from configuracao.models import Aluno, AnoLetivo, Curso, Docente, Fase, InscricaoTFC, Utilizador
from propostas.models import Proposta, Tecnologia
from tfc.models import TFC, TFCAluno

DOCENTES = ["Ana Martins", "Bruno Costa", "Carla Sousa"]
ALUNOS = [("22001", "Diogo Pereira", "LEI", 150), ("22002", "Eva Santos", "LEI", 132), ("22003", "Filipe Rocha", "LIG", 120),
          ("22004", "Gabriela Lima", "LEI", 96), ("22005", "Hugo Alves", "LIG", 60)]
PROPOSTAS = [
    ("DEMO01", "Plataforma de reporting de avaliações", "INDIVIDUAL_OU_GRUPO", ["Python", "Django", "PostgreSQL"], 0),
    ("DEMO02", "Aplicação móvel de acompanhamento de TFC", "INDIVIDUAL", ["React Native", "TypeScript"], 1),
    ("DEMO03", "Verificação automática de relatórios com GitHub Actions", "GRUPO", ["GitHub Actions", "Python"], 2),
    ("DEMO04", "Painel de indicadores para a coordenação", "INDIVIDUAL_OU_GRUPO", ["React", "Python"], 0),
    ("DEMO05", "Gestão de seminários e presenças", "INDIVIDUAL", ["Django", "PostgreSQL"], 1),
]
# aluno → propostas por ordem de preferência
CANDIDATURAS = {"22001": ["DEMO01", "DEMO04", "DEMO05"], "22002": ["DEMO01", "DEMO02", "DEMO04"],
                "22003": ["DEMO04", "DEMO05", "DEMO01"], "22004": ["DEMO02", "DEMO05", "DEMO04"],
                "22005": ["DEMO01", "DEMO02", "DEMO05"]}


class Command(BaseCommand):
    help = "Carrega dados de demonstração (ano letivo DEMO)."

    @transaction.atomic
    def handle(self, *args, **opts):
        agora = timezone.now()
        AnoLetivo.objects.filter(designacao="DEMO").exists() and self._apagar()
        ano = AnoLetivo.objects.create(designacao="DEMO", data_referencia_elegibilidade=agora.date())
        Fase.objects.create(ano_letivo=ano, tipo="CANDIDATURAS", data_inicio=agora - timedelta(days=7),
                            data_fim=agora + timedelta(days=30))

        docentes = []
        for i, nome in enumerate(DOCENTES, 1):
            u, _ = Utilizador.objects.get_or_create(username=f"demo_docente{i}",
                                                    defaults={"email": f"demo_docente{i}@exemplo.pt", "nome": nome})
            docentes.append(Docente.objects.get_or_create(utilizador=u)[0])

        alunos = {}
        for numero, nome, curso, ects in ALUNOS:
            u, _ = Utilizador.objects.get_or_create(username=f"demo_{numero}",
                                                    defaults={"email": f"demo_{numero}@exemplo.pt", "nome": nome})
            a, _ = Aluno.objects.get_or_create(utilizador=u, defaults={"numero": f"D{numero}",
                                                                        "curso": Curso.objects.get(codigo=curso)})
            InscricaoTFC.objects.create(aluno=a, ano_letivo=ano, ects=ects)
            alunos[numero] = a

        propostas = {}
        for codigo, titulo, modalidade, tecnologias, d in PROPOSTAS:
            p = Proposta.objects.create(
                ano_letivo=ano, codigo=codigo, titulo=titulo, descricao=f"Proposta de demonstração ({titulo}).",
                modalidade=modalidade, estado="DISPONIVEL", tipo_proponente="DOCENTE",
                proponente=docentes[d].utilizador, orientador_sugerido=docentes[d], data_publicacao=agora)
            p.cursos.set(Curso.objects.filter(codigo__in=["LEI", "LIG"]))
            p.tecnologias.set([Tecnologia.objects.get_or_create(nome=t)[0] for t in tecnologias])
            propostas[codigo] = p

        for numero, codigos in CANDIDATURAS.items():
            for codigo in codigos:
                if propostas[codigo].modalidade == "GRUPO":
                    continue
                Candidatura.objects.create(ano_letivo=ano, aluno=alunos[numero], proposta=propostas[codigo])

        # Atribuir o DEMO01 ao 1.º aluno: desencadeia as restantes operações na base de dados
        contemplada = Candidatura.objects.get(aluno=alunos["22001"], proposta=propostas["DEMO01"])
        with connection.cursor() as cur:
            cur.execute("SELECT atribuir_tfc(%s, %s)", [contemplada.id, docentes[0].id])

        self.stdout.write(self.style.SUCCESS("Dados de demonstração carregados no ano letivo DEMO."))
        for a in alunos.values():
            linhas = Candidatura.objects.filter(aluno=a, ano_letivo=ano).order_by("prioridade", "id")
            self.stdout.write(f"  {a.numero} {a.utilizador.nome}: " + ", ".join(
                f"{c.proposta.codigo}[{c.prioridade or '-'}:{c.get_estado_display()}]" for c in linhas))

    def _apagar(self):
        ano = AnoLetivo.objects.get(designacao="DEMO")
        ids = list(TFC.objects.filter(ano_letivo=ano).values_list("id", flat=True))
        TFCAluno.objects.filter(tfc_id__in=ids).delete()
        TFC.objects.filter(id__in=ids).delete()
        cand = list(Candidatura.objects.filter(ano_letivo=ano).values_list("id", flat=True))
        Historico.objects.filter(entidade="Candidatura", entidade_id__in=cand).delete()
        Candidatura.objects.filter(id__in=cand).delete()
        Proposta.objects.filter(ano_letivo=ano).delete()
        InscricaoTFC.objects.filter(ano_letivo=ano).delete()
        ano.fases.all().delete()
        ano.delete()
