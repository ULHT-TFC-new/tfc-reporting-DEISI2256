from rest_framework import serializers

from .models import Proposta


class PropostaSerializer(serializers.ModelSerializer):
    orientador = serializers.CharField(source="orientador_sugerido", default=None)
    cursos = serializers.SlugRelatedField(many=True, read_only=True, slug_field="codigo")
    tecnologias = serializers.SlugRelatedField(many=True, read_only=True, slug_field="nome")
    modalidade = serializers.CharField(source="get_modalidade_display")
    estado = serializers.CharField(source="get_estado_display")
    numero_candidaturas = serializers.IntegerField(read_only=True)

    class Meta:
        model = Proposta
        fields = ["id", "codigo", "titulo", "descricao", "area_aplicacao", "modalidade", "estado", "orientador",
                  "cursos", "tecnologias", "numero_candidaturas"]
