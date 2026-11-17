from django.test import TestCase


class HelloWorldTests(TestCase):
    def test_estado_responde_com_base_de_dados(self):
        resposta = self.client.get("/api/estado/")
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("PostgreSQL", resposta.json()["base_de_dados"])

    def test_lista_os_cursos_iniciais(self):
        resposta = self.client.get("/api/cursos/")
        self.assertEqual([c["codigo"] for c in resposta.json()], ["LCD", "LEI", "LIG"])

    def test_modelo_de_avaliacao_2026_27(self):
        from avaliacao.models import ModeloAvaliacao
        modelo = ModeloAvaliacao.objects.get(ano_letivo__designacao="2026/27", ativo=True)
        pesos = {m.nome: float(m.peso) for m in modelo.momentos.all()}
        self.assertEqual(pesos["Avaliação intercalar 1"] + pesos["Avaliação intercalar 2"]
                         + pesos["Avaliação final (1.ª época)"] + pesos["DEISIFest"], 100)
