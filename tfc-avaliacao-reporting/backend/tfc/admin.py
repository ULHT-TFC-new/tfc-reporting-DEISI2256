from django.contrib import admin

from .models import TFC, Atividade, Entrega, Pedido, TFCAluno, VerificacaoAutomatica


class TFCAlunoInline(admin.TabularInline):
    model = TFCAluno
    extra = 0
    fields = ["aluno", "ativo", "data_saida", "motivo_saida"]


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ["proposta", "ano_letivo", "estado", "orientador"]
    list_filter = ["ano_letivo", "estado"]
    inlines = [TFCAlunoInline]


@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ["tfc", "momento", "estado_relatorio", "estado", "data_submissao"]
    list_filter = ["momento", "estado", "estado_relatorio"]


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["tfc", "tipo", "estado", "data_pedido"]
    list_filter = ["tipo", "estado"]


admin.site.register([Atividade, VerificacaoAutomatica])
