"""TFC, acompanhamento e entregas (MP-03 a MP-05). Ver docs/03_modelo_de_dados.md, secção 3.4."""
from django.conf import settings
from django.db import models
from django.db.models import Q


class EstadoTFC(models.TextChoices):
    EM_CURSO = "EM_CURSO", "Em curso"
    ADIADO = "ADIADO", "Adiado para recurso"
    ENTREGUE = "ENTREGUE", "Entregue"
    AVALIADO = "AVALIADO", "Avaliado"
    CONCLUIDO = "CONCLUIDO", "Concluído"
    CANCELADO = "CANCELADO", "Cancelado"
    ARQUIVADO = "ARQUIVADO", "Arquivado"


class TipoPedido(models.TextChoices):
    DESISTENCIA = "DESISTENCIA", "Desistência"
    DESATRIBUICAO = "DESATRIBUICAO", "Desatribuição"
    ADIAMENTO = "ADIAMENTO", "Adiamento para a época de recurso"
    DISSOCIACAO = "DISSOCIACAO", "Dissociação do grupo"


class EstadoPedido(models.TextChoices):
    PENDENTE = "PENDENTE", "Pendente"
    VALIDADO = "VALIDADO", "Validado"
    REJEITADO = "REJEITADO", "Rejeitado"


class TipoAtividade(models.TextChoices):
    REUNIAO = "REUNIAO", "Reunião"
    ATIVIDADE = "ATIVIDADE", "Atividade"


class EstadoRelatorio(models.TextChoices):
    ENVIADO = "ENVIADO", "Enviado ao orientador"
    ACEITE = "ACEITE", "Aceite"
    DEVOLVIDO = "DEVOLVIDO", "Devolvido"


class EstadoEntrega(models.TextChoices):
    POR_SUBMETER = "POR_SUBMETER", "Por submeter"
    SUBMETIDA = "SUBMETIDA", "Submetida"
    EM_FALTA = "EM_FALTA", "Em falta"


class ResultadoVerificacao(models.TextChoices):
    CUMPRE = "CUMPRE", "Cumpre"
    NAO_CUMPRE = "NAO_CUMPRE", "Não cumpre"
    ERRO = "ERRO", "Erro na verificação"


class TFC(models.Model):
    proposta = models.OneToOneField("propostas.Proposta", on_delete=models.PROTECT, related_name="tfc")
    ano_letivo = models.ForeignKey("configuracao.AnoLetivo", on_delete=models.PROTECT, related_name="tfcs")
    estado = models.CharField(max_length=10, choices=EstadoTFC.choices, default=EstadoTFC.EM_CURSO)
    orientador = models.ForeignKey("configuracao.Docente", on_delete=models.PROTECT, related_name="orientacoes")
    coorientador = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="coorientacoes")
    repositorio_url = models.URLField(blank=True)
    data_atribuicao = models.DateTimeField(auto_now_add=True)
    epoca_final = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = "TFC"
        verbose_name_plural = "TFC"
        constraints = [models.CheckConstraint(condition=Q(epoca_final__in=[1, 2]), name="tfc_epoca_1_ou_2")]

    def __str__(self):
        return str(self.proposta)


class TFCAluno(models.Model):
    tfc = models.ForeignKey(TFC, on_delete=models.CASCADE, related_name="alunos")
    aluno = models.ForeignKey("configuracao.Aluno", on_delete=models.PROTECT, related_name="tfcs")
    ano_letivo = models.ForeignKey("configuracao.AnoLetivo", on_delete=models.PROTECT, related_name="+",
                                   help_text="Repetido do TFC para garantir um TFC ativo por aluno e ano.")
    candidatura = models.OneToOneField("candidaturas.Candidatura", null=True, blank=True, on_delete=models.SET_NULL,
                                       related_name="tfc_aluno")
    ativo = models.BooleanField(default=True)
    data_entrada = models.DateField(auto_now_add=True)
    data_saida = models.DateField(null=True, blank=True)
    motivo_saida = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "aluno do TFC"
        verbose_name_plural = "alunos dos TFC"
        constraints = [
            # R3: um aluno só tem um TFC ativo por ano
            models.UniqueConstraint(fields=["aluno", "ano_letivo"], condition=Q(ativo=True),
                                    name="um_tfc_ativo_por_aluno"),
        ]

    def __str__(self):
        return f"{self.aluno.numero} – {self.tfc}"


class Pedido(models.Model):
    """Desistência, desatribuição, adiamento ou dissociação: pedido, parecer do orientador e validação."""

    tfc = models.ForeignKey(TFC, on_delete=models.CASCADE, related_name="pedidos")
    tipo = models.CharField(max_length=15, choices=TipoPedido.choices)
    aluno = models.ForeignKey("configuracao.Aluno", null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    pedido_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="pedidos_feitos")
    motivo = models.TextField()
    parecer_orientador = models.TextField(blank=True)
    estado = models.CharField(max_length=10, choices=EstadoPedido.choices, default=EstadoPedido.PENDENTE)
    validado_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="pedidos_validados")
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_decisao = models.DateTimeField(null=True, blank=True)


class Atividade(models.Model):
    tfc = models.ForeignKey(TFC, on_delete=models.CASCADE, related_name="atividades")
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="+")
    tipo = models.CharField(max_length=10, choices=TipoAtividade.choices)
    data = models.DateField()
    descricao = models.TextField()

    class Meta:
        ordering = ["-data"]


class Entrega(models.Model):
    tfc = models.ForeignKey(TFC, on_delete=models.CASCADE, related_name="entregas")
    momento = models.ForeignKey("avaliacao.MomentoAvaliacao", on_delete=models.PROTECT, related_name="entregas")
    # Relatório (P-05.1 e P-05.2): só existe um ficheiro, o último enviado; guarda-se o caminho, não o ficheiro
    relatorio_caminho = models.CharField(max_length=500, blank=True)
    relatorio_data_envio = models.DateTimeField(null=True, blank=True)
    estado_relatorio = models.CharField(max_length=10, choices=EstadoRelatorio.choices, blank=True)
    comentario_orientador = models.TextField(blank=True)
    validado_por = models.ForeignKey("configuracao.Docente", null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="relatorios_validados")
    data_validacao = models.DateTimeField(null=True, blank=True)
    # Restantes entregáveis (P-05.3)
    link_repositorio = models.URLField(blank=True)
    commit_hash = models.CharField(max_length=40, blank=True)
    link_video = models.URLField(blank=True)
    link_versao_operacional = models.URLField(blank=True)
    texto_divulgacao = models.TextField(blank=True)
    imagem_caminho = models.CharField(max_length=500, blank=True)
    estado = models.CharField(max_length=15, choices=EstadoEntrega.choices, default=EstadoEntrega.POR_SUBMETER)
    submetida_por = models.ForeignKey("configuracao.Aluno", null=True, blank=True, on_delete=models.SET_NULL,
                                      related_name="+")
    data_submissao = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["tfc", "momento"], name="entrega_unica_por_momento")]

    def __str__(self):
        return f"{self.tfc} – {self.momento}"


class VerificacaoAutomatica(models.Model):
    """Resultado da verificação da entrega feita pelo DEISI2258."""

    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="verificacoes")
    resultado = models.CharField(max_length=10, choices=ResultadoVerificacao.choices)
    detalhes = models.JSONField(default=dict, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "verificação automática"
        verbose_name_plural = "verificações automáticas"
