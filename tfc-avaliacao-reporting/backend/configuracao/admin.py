from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (Aluno, AlunoUC, AnoLetivo, Curso, Docente, EntidadeExterna, Fase, GrupoCursos, InscricaoTFC,
                     UnidadeCurricular, Utilizador)


class FaseInline(admin.TabularInline):
    model = Fase
    extra = 0


@admin.register(AnoLetivo)
class AnoLetivoAdmin(admin.ModelAdmin):
    list_display = ["designacao", "estado", "ects_minimos", "min_candidaturas", "max_candidaturas"]
    inlines = [FaseInline]


@admin.register(Utilizador)
class UtilizadorAdmin(UserAdmin):
    list_display = ["username", "nome", "email", "is_active"]
    fieldsets = UserAdmin.fieldsets + (("Plataforma TFC", {"fields": ("nome", "entidade")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Plataforma TFC", {"fields": ("nome", "email")}),)


class AlunoUCInline(admin.TabularInline):
    model = AlunoUC
    extra = 0


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ["numero", "utilizador", "curso"]
    list_filter = ["curso"]
    search_fields = ["numero", "utilizador__nome"]
    inlines = [AlunoUCInline]


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ["utilizador", "departamento", "ativo"]
    list_filter = ["ativo"]


@admin.register(InscricaoTFC)
class InscricaoTFCAdmin(admin.ModelAdmin):
    list_display = ["aluno", "ano_letivo", "ects", "elegivel"]
    list_filter = ["ano_letivo", "elegivel"]


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nome", "ativo"]


admin.site.register([GrupoCursos, UnidadeCurricular, EntidadeExterna])
