"""Classes transversais: notificações (P-09.4) e histórico (R14)."""
from django.conf import settings
from django.db import models


class Notificacao(models.Model):
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notificacoes")
    tipo = models.CharField(max_length=50)
    mensagem = models.TextField()
    ligacao = models.CharField(max_length=300, blank=True)
    lida = models.BooleanField(default=False)
    email_enviado = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "notificação"
        verbose_name_plural = "notificações"
        ordering = ["-data"]


class Historico(models.Model):
    """Registo das mudanças de estado, prioridades, notas e dados publicados (preenchido por triggers)."""

    entidade = models.CharField(max_length=50)
    entidade_id = models.BigIntegerField()
    evento = models.CharField(max_length=100)
    campo = models.CharField(max_length=50, blank=True)
    valor_anterior = models.TextField(blank=True)
    valor_novo = models.TextField(blank=True)
    utilizador = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="+")
    data = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField(blank=True)

    class Meta:
        verbose_name = "registo do histórico"
        verbose_name_plural = "histórico"
        ordering = ["-data"]
        indexes = [models.Index(fields=["entidade", "entidade_id"])]
