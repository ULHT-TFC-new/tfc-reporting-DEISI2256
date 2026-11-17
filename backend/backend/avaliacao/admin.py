from django.contrib import admin

from .models import (Avaliacao, ClassificacaoCriterio, Criterio, Defesa, MembroJuri, ModeloAvaliacao,
                     MomentoAvaliacao, NotaMomento, Presenca, ResultadoFinal, Seminario)


class MomentoInline(admin.TabularInline):
    model = MomentoAvaliacao
    extra = 0
    fields = ["ordem", "nome", "tipo", "mecanismo", "peso", "conta_para", "epoca", "prazo_entrega", "prazo_avaliacao"]


@admin.register(ModeloAvaliacao)
class ModeloAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "niveis_escala", "limiar_discrepancia", "majoracao_orientador", "ativo"]
    inlines = [MomentoInline]


class CriterioInline(admin.TabularInline):
    model = Criterio
    extra = 0


@admin.register(MomentoAvaliacao)
class MomentoAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ["nome", "modelo", "tipo", "mecanismo", "peso", "conta_para", "prazo_entrega"]
    list_filter = ["modelo", "tipo"]
    inlines = [CriterioInline]


class ClassificacaoInline(admin.TabularInline):
    model = ClassificacaoCriterio
    extra = 0


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ["tfc", "momento", "jurado", "estado", "data_submissao"]
    list_filter = ["momento", "estado"]
    inlines = [ClassificacaoInline]


@admin.register(NotaMomento)
class NotaMomentoAdmin(admin.ModelAdmin):
    list_display = ["tfc_aluno", "momento", "valor", "estado"]
    list_filter = ["momento", "estado"]


@admin.register(ResultadoFinal)
class ResultadoFinalAdmin(admin.ModelAdmin):
    list_display = ["tfc_aluno", "epoca", "nota_final", "situacao", "estado"]
    list_filter = ["epoca", "situacao", "estado"]


admin.site.register([MembroJuri, Defesa, Seminario, Presenca])
