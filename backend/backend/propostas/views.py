from django.db.models import Count, Q
from rest_framework import viewsets

from candidaturas.models import NA_LISTA
from .models import EstadoProposta, Proposta
from .serializers import PropostaSerializer


class PropostaViewSet(viewsets.ReadOnlyModelViewSet):
    """Propostas disponíveis para candidatura (P-02.5), com filtros por curso, tecnologia e orientador."""

    serializer_class = PropostaSerializer

    def get_queryset(self):
        qs = (Proposta.objects.filter(estado=EstadoProposta.DISPONIVEL)
              .select_related("orientador_sugerido__utilizador")
              .prefetch_related("cursos", "tecnologias")
              .annotate(numero_candidaturas=Count("candidaturas", filter=Q(candidaturas__estado__in=NA_LISTA))))
        p = self.request.query_params
        if p.get("curso"):
            qs = qs.filter(cursos__codigo=p["curso"])
        if p.get("tecnologia"):
            qs = qs.filter(tecnologias__nome__iexact=p["tecnologia"])
        if p.get("orientador"):
            qs = qs.filter(orientador_sugerido__utilizador__nome__icontains=p["orientador"])
        if p.get("pesquisa"):
            qs = qs.filter(Q(titulo__icontains=p["pesquisa"]) | Q(descricao__icontains=p["pesquisa"]))
        return qs.distinct()
