"""Propostas de TFC (MP-02). Ver docs/03_modelo_de_dados.md, secção 3.2."""
from django.conf import settings
from django.db import models


class Modalidade(models.TextChoices):
    INDIVIDUAL = "INDIVIDUAL", "Individual"
    GRUPO = "GRUPO", "Em grupo"
    INDIVIDUAL_OU_GRUPO = "INDIVIDUAL_OU_GRUPO", "Individual ou em grupo"


class EstadoProposta(models.TextChoices):
    EM_VALIDACAO = "EM_VALIDACAO", "Em validação"
    ALTERACOES_SOLICITADAS = "ALTERACOES_SOLICITADAS", "Alterações solicitadas"
    ACEITE = "ACEITE", "Aceite"
    RECUSADA = "RECUSADA", "Recusada"
    DISPONIVEL = "DISPONIVEL", "Disponível"
    PRE_ATRIBUIDA = "PRE_ATRIBUIDA", "Pré-atribuída"
    ATRIBUIDA = "ATRIBUIDA", "Atribuída"
    ARQUIVADA = "ARQUIVADA", "Arquivada"


class TipoProponente(models.TextChoices):
    DOCENTE = "DOCENTE", "Docente"
    ALUNO = "ALUNO", "Aluno"
    EMPRESA = "EMPRESA", "Empresa ou instituição"
    DEPARTAMENTO = "DEPARTAMENTO", "Outro departamento"


class TipoLigacaoUC(models.TextChoices):
    REQUISITO_CONCLUIDA = "REQUISITO_CONCLUIDA", "Requisito: UC concluída"
    REQUISITO_EM_CURSO = "REQUISITO_EM_CURSO", "Requisito: UC em curso"
    ASSOCIADA = "ASSOCIADA", "Disciplina associada"


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Proposta(models.Model):
    ano_letivo = models.ForeignKey("configuracao.AnoLetivo", on_delete=models.PROTECT, related_name="propostas")
    codigo = models.CharField(max_length=20, unique=True, null=True, blank=True, help_text='Por exemplo "DEISI2257".')
    titulo = models.CharField(max_length=300)
    descricao = models.TextField()
    area_aplicacao = models.CharField(max_length=200, blank=True)
    modalidade = models.CharField(max_length=20, choices=Modalidade.choices)
    estado = models.CharField(max_length=25, choices=EstadoProposta.choices, default=EstadoProposta.EM_VALIDACAO)
    tipo_proponente = models.CharField(max_length=15, choices=TipoProponente.choices)
    proponente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="propostas")
    entidade = models.ForeignKey("configuracao.EntidadeExterna", null=True, blank=True, on_delete=models.PROTECT,
                                 related_name="propostas")
    orientador_sugerido = models.ForeignKey("configuracao.Docente", null=True, blank=True, on_delete=models.SET_NULL,
                                            related_name="propostas_sugeridas")
    coorientador_sugerido = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                                              on_delete=models.SET_NULL, related_name="coorientacoes_sugeridas")
    continuacao_de = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL,
                                       related_name="continuacoes")
    cursos = models.ManyToManyField("configuracao.Curso", related_name="propostas")
    tecnologias = models.ManyToManyField(Tecnologia, blank=True, related_name="propostas")
    notas_internas = models.TextField(blank=True, help_text="Visíveis apenas para docentes e coordenação.")
    data_submissao = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["codigo", "titulo"]

    def __str__(self):
        return f"{self.codigo or '—'} {self.titulo}"


class PropostaUC(models.Model):
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name="ucs")
    uc = models.ForeignKey("configuracao.UnidadeCurricular", on_delete=models.PROTECT, related_name="propostas")
    tipo = models.CharField(max_length=20, choices=TipoLigacaoUC.choices)

    class Meta:
        verbose_name = "UC da proposta"
        verbose_name_plural = "UCs das propostas"
        constraints = [models.UniqueConstraint(fields=["proposta", "uc"], name="proposta_uc_unica")]


class PropostaAluno(models.Model):
    """Aluno indicado ou pré-selecionado numa proposta."""

    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name="alunos_indicados")
    aluno = models.ForeignKey("configuracao.Aluno", on_delete=models.CASCADE, related_name="propostas_indicadas")

    class Meta:
        verbose_name = "aluno indicado"
        verbose_name_plural = "alunos indicados"
        constraints = [models.UniqueConstraint(fields=["proposta", "aluno"], name="proposta_aluno_unico")]


class AnexoProposta(models.Model):
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name="anexos")
    caminho_ficheiro = models.CharField(max_length=500)
    nome_original = models.CharField(max_length=255)

    class Meta:
        verbose_name = "anexo"
        verbose_name_plural = "anexos"
