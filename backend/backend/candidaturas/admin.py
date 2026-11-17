from django.contrib import admin

from .models import Candidatura, Grupo, Selecao


@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ["aluno", "proposta", "grupo", "prioridade", "estado", "motivo_fim"]
    list_filter = ["ano_letivo", "estado"]
    search_fields = ["aluno__numero", "proposta__codigo"]


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "ano_letivo", "origem", "estado"]
    list_filter = ["estado", "origem"]


admin.site.register(Selecao)
