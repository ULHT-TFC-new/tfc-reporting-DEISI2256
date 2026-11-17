"""Candidaturas e atribuição (MP-03). Ver docs/03_modelo_de_dados.md, secção 3.3.

As regras da lista de candidaturas (prioridade, renumeração e validação) estão em triggers
do PostgreSQL, criados na migração 0002 desta app.
"""
from django.conf import settings
from django.db import models
from django.db.models import Q


class OrigemGrupo(models.TextChoices):
    CANDIDATURA = "CANDIDATURA", "Candidatura em grupo"
    JUNCAO = "JUNCAO", "Junção pelo docente"


class EstadoGrupo(models.TextChoices):
    PENDENTE = "PENDENTE", "Pendente"
    ATIVO = "ATIVO", "Ativo"
    RECUSADO = "RECUSADO", "Recusado"
    DISSOLVIDO = "DISSOLVIDO", "Dissolvido"


class EstadoCandidatura(models.TextChoices):
    PENDENTE_CONFIRMACAO = "PENDENTE_CONFIRMACAO", "Pendente de confirmação"
    ATIVA = "ATIVA", "Ativa"
    RECUSADA = "RECUSADA", "Recusada"
    CONTEMPLADA = "CONTEMPLADA", "Contemplada"
    ENCERRADA = "ENCERRADA", "Encerrada"
    CANCELADA = "CANCELADA", "Cancelada"


class MotivoFim(models.TextChoices):
    SEM_CREDITOS = "SEM_CREDITOS", "Sem os créditos exigidos"
    TFC_ATRIBUIDO_A_OUTRO = "TFC_ATRIBUIDO_A_OUTRO", "TFC atribuído a outro candidato"
    ALUNO_CONTEMPLADO = "ALUNO_CONTEMPLADO", "Aluno já contemplado"
    RECUSADA_PELO_COLEGA = "RECUSADA_PELO_COLEGA", "Recusada pelo colega"
    SEM_CONFIRMACAO = "SEM_CONFIRMACAO", "Sem confirmação a tempo"
    DESISTENCIA = "DESISTENCIA", "Desistência"
    CANCELADA_PELO_ALUNO = "CANCELADA_PELO_ALUNO", "Cancelada pelo aluno"
    SUBSTITUIDA = "SUBSTITUIDA", "Substituída"


NA_LISTA = [EstadoCandidatura.PENDENTE_CONFIRMACAO, EstadoCandidatura.ATIVA]


class Grupo(models.Model):
    ano_letivo = models.ForeignKey("configuracao.AnoLetivo", on_delete=models.PROTECT, related_name="grupos")
    submissor = models.ForeignKey("configuracao.Aluno", on_delete=models.PROTECT, related_name="grupos_submetidos")
    colega = models.ForeignKey("configuracao.Aluno", on_delete=models.PROTECT, related_name="grupos_como_colega")
    origem = models.CharField(max_length=15, choices=OrigemGrupo.choices, default=OrigemGrupo.CANDIDATURA)
    estado = models.CharField(max_length=10, choices=EstadoGrupo.choices, default=EstadoGrupo.PENDENTE)
    proposto_por = models.ForeignKey("configuracao.Docente", null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="juncoes_propostas", help_text="Docente que propôs a junção (P-03.8).")
    aceite_submissor = models.BooleanField(default=True)
    aceite_colega = models.BooleanField(default=False)
    validado_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="+")
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(condition=~Q(submissor=models.F("colega")), name="grupo_alunos_diferentes"),
            # R4: um aluno só está num grupo ativo por ano
            models.UniqueConstraint(fields=["ano_letivo", "submissor"], condition=Q(estado="ATIVO"),
                                    name="grupo_ativo_unico_submissor"),
            models.UniqueConstraint(fields=["ano_letivo", "colega"], condition=Q(estado="ATIVO"),
                                    name="grupo_ativo_unico_colega"),
        ]

    def __str__(self):
        return f"{self.submissor.numero} + {self.colega.numero}"


class Candidatura(models.Model):
    ano_letivo = models.ForeignKey("configuracao.AnoLetivo", on_delete=models.PROTECT, related_name="candidaturas")
    proposta = models.ForeignKey("propostas.Proposta", on_delete=models.PROTECT, related_name="candidaturas")
    aluno = models.ForeignKey("configuracao.Aluno", on_delete=models.PROTECT, related_name="candidaturas",
                              help_text="Candidato individual ou aluno que submete a candidatura do grupo.")
    grupo = models.ForeignKey(Grupo, null=True, blank=True, on_delete=models.PROTECT, related_name="candidaturas")
    prioridade = models.PositiveSmallIntegerField(null=True, blank=True,
                                                  help_text="Só existe enquanto a candidatura está na lista.")
    estado = models.CharField(max_length=25, choices=EstadoCandidatura.choices, default=EstadoCandidatura.ATIVA)
    motivo_fim = models.CharField(max_length=25, choices=MotivoFim.choices, blank=True)
    substitui = models.OneToOneField("self", null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="substituida_por")
    data_submissao = models.DateTimeField(auto_now_add=True)
    data_estado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["aluno", "prioridade"]
        constraints = [
            # R1: um aluno não se candidata duas vezes ao mesmo TFC
            models.UniqueConstraint(fields=["proposta", "aluno"], condition=Q(estado__in=NA_LISTA),
                                    name="candidatura_unica_por_tfc"),
            # R2: sem prioridades repetidas na lista (individual e de grupo)
            models.UniqueConstraint(fields=["ano_letivo", "aluno", "prioridade"],
                                    condition=Q(grupo__isnull=True, estado__in=NA_LISTA),
                                    name="prioridade_unica_individual"),
            models.UniqueConstraint(fields=["grupo", "prioridade"],
                                    condition=Q(grupo__isnull=False, estado__in=NA_LISTA),
                                    name="prioridade_unica_grupo"),
        ]

    def __str__(self):
        return f"{self.aluno.numero} → {self.proposta} ({self.get_estado_display()})"


class Selecao(models.Model):
    """Ordenação dos candidatos de uma proposta e ajustes da coordenação (P-03.7)."""

    proposta = models.ForeignKey("propostas.Proposta", on_delete=models.CASCADE, related_name="selecoes")
    candidatura = models.OneToOneField(Candidatura, on_delete=models.CASCADE, related_name="selecao")
    posicao = models.PositiveSmallIntegerField()
    pontuacao = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    justificacao_ajuste = models.TextField(blank=True)
    confirmada = models.BooleanField(default=False)
    confirmada_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                       related_name="+")

    class Meta:
        verbose_name = "seleção"
        verbose_name_plural = "seleções"
        ordering = ["proposta", "posicao"]
