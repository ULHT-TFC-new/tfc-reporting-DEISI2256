"""Dados iniciais: ano letivo 2026/27 com as fases do regulamento, cursos e grupo de cursos."""
from datetime import date, datetime
from zoneinfo import ZoneInfo

from django.db import migrations

LX = ZoneInfo("Europe/Lisbon")

FASES = [  # Regulamento de TFC 2026/27, "Datas importantes" (Anexo A de docs/02_processos.md)
    ("PROPOSTAS_DOCENTES", (2026, 9, 1), (2026, 9, 30)),
    ("PROPOSTAS_EXTERNAS", (2026, 9, 1), (2026, 9, 30)),
    ("PROPOSTAS_ALUNOS", (2026, 9, 10), (2026, 9, 27)),
    ("VALIDACAO_PROPOSTAS_ALUNOS", (2026, 9, 11), (2026, 9, 30)),
    ("CANDIDATURAS", (2026, 9, 9), (2026, 10, 4)),
    ("LISTA_FINAL", (2026, 10, 5), (2026, 10, 5)),
]

CURSOS = [
    ("LEI", "Licenciatura em Engenharia Informática"),
    ("LIG", "Licenciatura em Informática de Gestão"),
    ("LCD", "Licenciatura em Ciência de Dados"),
]


def criar(apps, schema_editor):
    AnoLetivo = apps.get_model("configuracao", "AnoLetivo")
    Fase = apps.get_model("configuracao", "Fase")
    Curso = apps.get_model("configuracao", "Curso")
    GrupoCursos = apps.get_model("configuracao", "GrupoCursos")

    ano, _ = AnoLetivo.objects.get_or_create(
        designacao="2026/27", defaults={"data_referencia_elegibilidade": date(2026, 10, 4)})
    for tipo, inicio, fim in FASES:
        Fase.objects.get_or_create(
            ano_letivo=ano, tipo=tipo,
            defaults={"data_inicio": datetime(*inicio, 0, 0, tzinfo=LX),
                      "data_fim": datetime(*fim, 23, 59, 59, tzinfo=LX)})
    cursos = {c: Curso.objects.get_or_create(codigo=c, defaults={"nome": n})[0] for c, n in CURSOS}
    grupo, _ = GrupoCursos.objects.get_or_create(nome="LEI + LIG")
    grupo.cursos.set([cursos["LEI"], cursos["LIG"]])


class Migration(migrations.Migration):
    dependencies = [("configuracao", "0001_initial")]
    operations = [migrations.RunPython(criar, migrations.RunPython.noop)]
