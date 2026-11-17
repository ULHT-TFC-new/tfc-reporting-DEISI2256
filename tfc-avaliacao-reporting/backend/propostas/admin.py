from django.contrib import admin

from .models import AnexoProposta, Proposta, PropostaAluno, PropostaUC, Tecnologia


class PropostaUCInline(admin.TabularInline):
    model = PropostaUC
    extra = 0


class PropostaAlunoInline(admin.TabularInline):
    model = PropostaAluno
    extra = 0


@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ["codigo", "titulo", "modalidade", "estado", "tipo_proponente", "orientador_sugerido"]
    list_filter = ["ano_letivo", "estado", "modalidade", "tipo_proponente"]
    search_fields = ["codigo", "titulo"]
    filter_horizontal = ["cursos", "tecnologias"]
    inlines = [PropostaUCInline, PropostaAlunoInline]


admin.site.register([Tecnologia, AnexoProposta])
