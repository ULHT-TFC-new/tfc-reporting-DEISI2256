from django.contrib import admin

from .models import Historico, Notificacao


@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ["data", "entidade", "entidade_id", "evento", "campo", "valor_anterior", "valor_novo"]
    list_filter = ["entidade", "evento"]


@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ["destinatario", "tipo", "lida", "data"]
