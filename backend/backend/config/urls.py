from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from configuracao.views import CursoViewSet, estado
from propostas.views import PropostaViewSet

router = DefaultRouter()
router.register("cursos", CursoViewSet)
router.register("propostas", PropostaViewSet, basename="proposta")

admin.site.site_header = "Plataforma de gestão de TFC"
admin.site.site_title = "TFC DEISI"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/estado/", estado, name="estado"),
    path("api/", include(router.urls)),
]
