"""Modelo de avaliação de 2026/27 (regulamento, cap. 5 e 6; Anexo A de docs/02_processos.md).

Os critérios de cada momento ainda não estão carregados: são definidos pela coordenação (P-06.2).
"""
from datetime import datetime
from zoneinfo import ZoneInfo

from django.db import migrations

LX = ZoneInfo("Europe/Lisbon")


def d(a, m, dia, h=23, mi=59):
    return datetime(a, m, dia, h, mi, tzinfo=LX)


MOMENTOS = [
    # ordem, nome, tipo, mecanismo, com_nota, peso, época, requer entrega, prazo de entrega, publicação
    (1, "Avaliação intercalar 1", "INTERCALAR", "JURI_CRITERIOS", True, 20, None, True, d(2026, 12, 13), (2027, 1, 4)),
    (2, "Avaliação intercalar 2", "INTERCALAR", "JURI_CRITERIOS", True, 20, None, True, d(2027, 4, 4), (2027, 4, 18)),
    (3, "Avaliação final (1.ª época)", "FINAL", "JURI_CRITERIOS", True, 55, 1, True, d(2027, 6, 4), None),
    (4, "Avaliação final (2.ª época)", "FINAL", "JURI_CRITERIOS", True, 55, 2, True, d(2027, 7, 2), None),
    (5, "DEISIFest", "DEISIFEST", "VOTACAO", True, 5, None, False, None, None),
    (6, "Seminários", "PRESENCAS", "PRESENCA", False, 0, None, False, None, None),
]


def criar(apps, schema_editor):
    AnoLetivo = apps.get_model("configuracao", "AnoLetivo")
    ModeloAvaliacao = apps.get_model("avaliacao", "ModeloAvaliacao")
    MomentoAvaliacao = apps.get_model("avaliacao", "MomentoAvaliacao")
    from datetime import date

    ano = AnoLetivo.objects.get(designacao="2026/27")
    modelo, criado = ModeloAvaliacao.objects.get_or_create(ano_letivo=ano, versao=1, defaults={"ativo": True})
    if not criado:
        return
    for ordem, nome, tipo, mec, com_nota, peso, epoca, entrega, prazo, publ in MOMENTOS:
        MomentoAvaliacao.objects.create(
            modelo=modelo, ordem=ordem, nome=nome, tipo=tipo, mecanismo=mec, com_nota=com_nota, peso=peso,
            epoca=epoca, requer_entrega=entrega, prazo_entrega=prazo,
            data_publicacao=date(*publ) if publ else None)


class Migration(migrations.Migration):
    dependencies = [("avaliacao", "0002_initial"), ("configuracao", "0002_dados_iniciais")]
    operations = [migrations.RunPython(criar, migrations.RunPython.noop)]
