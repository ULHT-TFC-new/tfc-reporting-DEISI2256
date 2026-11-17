from django.db import connection
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Curso
from .serializers import CursoSerializer


@api_view(["GET"])
def estado(request):
    """Verifica que o backend responde e que a ligação à base de dados funciona."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT version()")
        versao = cursor.fetchone()[0]
    return Response({"backend": "ok", "base_de_dados": versao})


class CursoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Curso.objects.filter(ativo=True)
    serializer_class = CursoSerializer
