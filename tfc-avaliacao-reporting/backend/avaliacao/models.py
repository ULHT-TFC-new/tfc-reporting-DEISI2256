"""Avaliação e resultados (MP-06 a MP-08). Ver docs/03_modelo_de_dados.md, secção 3.5."""
from django.conf import settings
from django.db import models
from django.db.models import Q


class TipoMomento(models.TextChoices):
    INTERCALAR = "INTERCALAR", "Avaliação intercalar"
    FINAL = "FINAL", "Avaliação final"
    DEISIFEST = "DEISIFEST", "DEISIFest"
    PRESENCAS = "PRESENCAS", "Presenças"
    OUTRO = "OUTRO", "Outro momento"


class Mecanismo(models.TextChoices):
    JURI_CRITERIOS = "JURI_CRITERIOS", "Júri com critérios"
    VOTACAO = "VOTACAO", "Votação"
    PRESENCA = "PRESENCA", "Registo de presença"


class EstadoAvaliacao(models.TextChoices):
    RASCUNHO = "RASCUNHO", "Rascunho"
    SUBMETIDA = "SUBMETIDA", "Submetida"


class OrigemNota(models.TextChoices):
    CALCULADA = "CALCULADA", "Calculada"
    VOTACAO = "VOTACAO", "Votação"
    MANUAL = "MANUAL", "Manual"


class EstadoNota(models.TextChoices):
    CALCULADA = "CALCULADA", "Calculada"
    CONFIRMADA = "CONFIRMADA", "Confirmada"
    PUBLICADA = "PUBLICADA", "Publicada"


class Situacao(models.TextChoices):
    APROVADO = "APROVADO", "Aprovado"
    REPROVADO = "REPROVADO", "Reprovado"
    EXCLUIDO = "EXCLUIDO", "Excluído"


class ModeloAvaliacao(models.Model):
    ano_letivo = models.ForeignKey("configuracao.AnoLetivo", on_delete=models.PROTECT, related_name="modelos_avaliacao")
    versao = models.PositiveSmallIntegerField(default=1)
    niveis_escala = models.PositiveSmallIntegerField(default=10)
    limiar_discrepancia = models.PositiveSmallIntegerField(default=2)
    majoracao_orientador = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    ativo = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "modelo de avaliação"
        verbose_name_plural = "modelos de avaliação"
        constraints = [
            models.UniqueConstraint(fields=["ano_letivo", "versao"], name="modelo_versao_unica"),
            models.UniqueConstraint(fields=["ano_letivo"], condition=Q(ativo=True), name="um_modelo_ativo_por_ano"),
        ]

    def __str__(self):
        return f"{self.ano_letivo} v{self.versao}"


class MomentoAvaliacao(models.Model):
    modelo = models.ForeignKey(ModeloAvaliacao, on_delete=models.CASCADE, related_name="momentos")
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=15, choices=TipoMomento.choices)
    mecanismo = models.CharField(max_length=15, choices=Mecanismo.choices)
    com_nota = models.BooleanField(default=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="Percentagem.")
    conta_para = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT, related_name="componentes",
                                   help_text="Vazio = conta para a nota final (P-06.3).")
    epoca = models.PositiveSmallIntegerField(null=True, blank=True, help_text="Só para a avaliação final (1 ou 2).")
    requer_entrega = models.BooleanField(default=False)
    prazo_entrega = models.DateTimeField(null=True, blank=True)
    prazo_avaliacao = models.DateTimeField(null=True, blank=True)
    data_publicacao = models.DateField(null=True, blank=True)
    ordem = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "momento de avaliação"
        verbose_name_plural = "momentos de avaliação"
        ordering = ["modelo", "ordem"]
        constraints = [
            models.CheckConstraint(condition=Q(peso__gte=0, peso__lte=100), name="momento_peso_0_100"),
            models.CheckConstraint(condition=Q(epoca__isnull=True) | Q(epoca__in=[1, 2]), name="momento_epoca_1_ou_2"),
        ]

    def __str__(self):
        return self.nome


class Criterio(models.Model):
    momento = models.ForeignKey(MomentoAvaliacao, on_delete=models.CASCADE, related_name="criterios")
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    ordem = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "critério"
        verbose_name_plural = "critérios"
        ordering = ["momento", "ordem"]
        constraints = [models.CheckConstraint(condition=Q(peso__gt=0, peso__lte=100), name="criterio_peso_0_100")]

    def __str__(self):
        return self.nome


class MembroJuri(models.Model):
    tfc = models.ForeignKey("tfc.TFC", on_delete=models.CASCADE, related_name="juri")
    momento = models.ForeignKey(MomentoAvaliacao, on_delete=models.PROTECT, related_name="juri")
    docente = models.ForeignKey("configuracao.Docente", on_delete=models.PROTECT, related_name="juris")

    class Meta:
        verbose_name = "membro do júri"
        verbose_name_plural = "membros do júri"
        constraints = [models.UniqueConstraint(fields=["tfc", "momento", "docente"], name="jurado_unico")]


class Defesa(models.Model):
    tfc = models.ForeignKey("tfc.TFC", on_delete=models.CASCADE, related_name="defesas")
    momento = models.ForeignKey(MomentoAvaliacao, on_delete=models.PROTECT, related_name="defesas")
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=200)
    publicada_em = models.DateTimeField(null=True, blank=True)


class Avaliacao(models.Model):
    tfc = models.ForeignKey("tfc.TFC", on_delete=models.CASCADE, related_name="avaliacoes")
    momento = models.ForeignKey(MomentoAvaliacao, on_delete=models.PROTECT, related_name="avaliacoes")
    jurado = models.ForeignKey("configuracao.Docente", on_delete=models.PROTECT, related_name="avaliacoes")
    estado = models.CharField(max_length=10, choices=EstadoAvaliacao.choices, default=EstadoAvaliacao.RASCUNHO)
    apreciacao = models.TextField(blank=True, help_text="Aceita Markdown.")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_submissao = models.DateTimeField(null=True, blank=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "avaliação"
        verbose_name_plural = "avaliações"
        constraints = [models.UniqueConstraint(fields=["tfc", "momento", "jurado"], name="avaliacao_unica_por_jurado")]


class ClassificacaoCriterio(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name="classificacoes")
    criterio = models.ForeignKey(Criterio, on_delete=models.PROTECT, related_name="classificacoes")
    nivel = models.PositiveSmallIntegerField()
    justificacao_discrepancia = models.TextField(blank=True)

    class Meta:
        verbose_name = "classificação por critério"
        verbose_name_plural = "classificações por critério"
        constraints = [
            models.UniqueConstraint(fields=["avaliacao", "criterio"], name="classificacao_unica"),
            models.CheckConstraint(condition=Q(nivel__gte=1, nivel__lte=10), name="nivel_1_a_10"),
        ]


class Seminario(models.Model):
    momento = models.ForeignKey(MomentoAvaliacao, on_delete=models.CASCADE, related_name="seminarios")
    titulo = models.CharField(max_length=200)
    data = models.DateField()

    class Meta:
        verbose_name = "seminário"
        ordering = ["data"]

    def __str__(self):
        return self.titulo


class Presenca(models.Model):
    seminario = models.ForeignKey(Seminario, on_delete=models.CASCADE, related_name="presencas")
    aluno = models.ForeignKey("configuracao.Aluno", on_delete=models.CASCADE, related_name="presencas")
    presente = models.BooleanField(default=True)
    registado_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="+")

    class Meta:
        verbose_name = "presença"
        constraints = [models.UniqueConstraint(fields=["seminario", "aluno"], name="presenca_unica")]


class NotaMomento(models.Model):
    tfc_aluno = models.ForeignKey("tfc.TFCAluno", on_delete=models.PROTECT, related_name="notas")
    momento = models.ForeignKey(MomentoAvaliacao, on_delete=models.PROTECT, related_name="notas")
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    origem = models.CharField(max_length=10, choices=OrigemNota.choices, default=OrigemNota.CALCULADA)
    estado = models.CharField(max_length=10, choices=EstadoNota.choices, default=EstadoNota.CALCULADA)
    confirmada_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                       related_name="+")
    data_publicacao = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "nota do momento"
        verbose_name_plural = "notas dos momentos"
        constraints = [
            models.UniqueConstraint(fields=["tfc_aluno", "momento"], name="nota_unica_por_momento"),
            models.CheckConstraint(condition=Q(valor__gte=0, valor__lte=20), name="nota_momento_0_20"),
        ]


class ResultadoFinal(models.Model):
    tfc_aluno = models.ForeignKey("tfc.TFCAluno", on_delete=models.PROTECT, related_name="resultados")
    epoca = models.PositiveSmallIntegerField(default=1)
    nota_final = models.PositiveSmallIntegerField()
    situacao = models.CharField(max_length=10, choices=Situacao.choices)
    percentagem_presencas = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=EstadoNota.choices, default=EstadoNota.CALCULADA)
    data_publicacao = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "resultado final"
        verbose_name_plural = "resultados finais"
        constraints = [
            models.UniqueConstraint(fields=["tfc_aluno", "epoca"], name="resultado_unico_por_epoca"),
            models.CheckConstraint(condition=Q(nota_final__lte=20), name="nota_final_0_20"),
        ]
