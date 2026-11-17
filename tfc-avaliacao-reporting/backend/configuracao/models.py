"""Configuração do ano letivo e utilizadores (MP-01). Ver docs/03_modelo_de_dados.md, secção 3.1."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q


class EstadoAnoLetivo(models.TextChoices):
    ABERTO = "ABERTO", "Aberto"
    FECHADO = "FECHADO", "Fechado"


class TipoFase(models.TextChoices):
    PROPOSTAS_DOCENTES = "PROPOSTAS_DOCENTES", "Propostas de docentes"
    PROPOSTAS_EXTERNAS = "PROPOSTAS_EXTERNAS", "Propostas de empresas e departamentos"
    PROPOSTAS_ALUNOS = "PROPOSTAS_ALUNOS", "Propostas de alunos"
    VALIDACAO_PROPOSTAS_ALUNOS = "VALIDACAO_PROPOSTAS_ALUNOS", "Validação das propostas de alunos"
    CANDIDATURAS = "CANDIDATURAS", "Candidaturas"
    LISTA_FINAL = "LISTA_FINAL", "Lista final de atribuídos"


class EstadoUC(models.TextChoices):
    CONCLUIDA = "CONCLUIDA", "Concluída"
    EM_CURSO = "EM_CURSO", "Em curso"


class TipoEntidade(models.TextChoices):
    EMPRESA = "EMPRESA", "Empresa ou instituição"
    DEPARTAMENTO = "DEPARTAMENTO", "Outro departamento"


class AnoLetivo(models.Model):
    designacao = models.CharField(max_length=9, unique=True, help_text='Por exemplo "2026/27".')
    data_referencia_elegibilidade = models.DateField()
    ects_minimos = models.PositiveSmallIntegerField(default=90)
    min_candidaturas = models.PositiveSmallIntegerField(default=3)
    max_candidaturas = models.PositiveSmallIntegerField(default=6)
    max_orientacoes_sugeridas = models.PositiveSmallIntegerField(default=5)
    antecedencia_relatorio_dias = models.PositiveSmallIntegerField(default=7)
    estado = models.CharField(max_length=10, choices=EstadoAnoLetivo.choices, default=EstadoAnoLetivo.ABERTO)
    data_fecho = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "ano letivo"
        verbose_name_plural = "anos letivos"
        ordering = ["-designacao"]
        constraints = [
            models.CheckConstraint(condition=Q(min_candidaturas__lte=models.F("max_candidaturas")),
                                   name="ano_min_max_candidaturas"),
        ]

    def __str__(self):
        return self.designacao


class Fase(models.Model):
    ano_letivo = models.ForeignKey(AnoLetivo, on_delete=models.CASCADE, related_name="fases")
    tipo = models.CharField(max_length=30, choices=TipoFase.choices)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    class Meta:
        ordering = ["data_inicio"]
        constraints = [
            models.UniqueConstraint(fields=["ano_letivo", "tipo"], name="fase_unica_por_ano"),
            models.CheckConstraint(condition=Q(data_fim__gt=models.F("data_inicio")), name="fase_fim_depois_inicio"),
        ]

    def __str__(self):
        return f"{self.ano_letivo} – {self.get_tipo_display()}"


class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["codigo"]

    def __str__(self):
        return self.codigo


class GrupoCursos(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cursos = models.ManyToManyField(Curso, related_name="grupos")
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "grupo de cursos"
        verbose_name_plural = "grupos de cursos"

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name = "unidade curricular"
        verbose_name_plural = "unidades curriculares"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class EntidadeExterna(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=15, choices=TipoEntidade.choices)
    contacto = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "entidade externa"
        verbose_name_plural = "entidades externas"

    def __str__(self):
        return self.nome


class Utilizador(AbstractUser):
    """Utilizador da plataforma. Os perfis são grupos do Django (aluno, docente, coordenação...)."""

    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=200)
    entidade = models.ForeignKey(EntidadeExterna, null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name="representantes")

    class Meta:
        verbose_name = "utilizador"
        verbose_name_plural = "utilizadores"

    def __str__(self):
        return self.nome or self.username


class Aluno(models.Model):
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, related_name="aluno")
    numero = models.CharField(max_length=20, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="alunos")

    class Meta:
        ordering = ["numero"]

    def __str__(self):
        return f"{self.numero} – {self.utilizador}"


class AlunoUC(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="ucs")
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.PROTECT, related_name="alunos")
    estado = models.CharField(max_length=10, choices=EstadoUC.choices)
    nota = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "UC do aluno"
        verbose_name_plural = "UCs dos alunos"
        constraints = [
            models.UniqueConstraint(fields=["aluno", "uc"], name="aluno_uc_unica"),
            models.CheckConstraint(condition=Q(nota__isnull=True) | Q(nota__gte=0, nota__lte=20), name="aluno_uc_nota_0_20"),
        ]


class InscricaoTFC(models.Model):
    """Inscrição do aluno na UC de TFC num ano letivo, com os ECTS na data de referência."""

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="inscricoes")
    ano_letivo = models.ForeignKey(AnoLetivo, on_delete=models.PROTECT, related_name="inscricoes")
    ects = models.PositiveSmallIntegerField()
    elegivel = models.BooleanField(default=False, help_text="ECTS iguais ou superiores ao mínimo do ano.")

    class Meta:
        verbose_name = "inscrição em TFC"
        verbose_name_plural = "inscrições em TFC"
        constraints = [models.UniqueConstraint(fields=["aluno", "ano_letivo"], name="inscricao_unica_por_ano")]

    def save(self, *args, **kwargs):
        self.elegivel = self.ects >= self.ano_letivo.ects_minimos
        super().save(*args, **kwargs)


class Docente(models.Model):
    utilizador = models.OneToOneField(Utilizador, on_delete=models.CASCADE, related_name="docente")
    departamento = models.CharField(max_length=100, default="DEISI")
    ativo = models.BooleanField(default=True, help_text="Só os docentes ativos aparecem nas listas de escolha.")

    class Meta:
        ordering = ["utilizador__nome"]

    def __str__(self):
        return str(self.utilizador)
