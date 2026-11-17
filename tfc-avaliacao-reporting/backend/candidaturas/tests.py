"""Testes das regras da lista de candidaturas e da atribuição, implementadas no PostgreSQL."""
from datetime import timedelta

from django.db import DatabaseError, connection, transaction
from django.test import TestCase
from django.utils import timezone

from configuracao.models import Aluno, AnoLetivo, Curso, Docente, Fase, InscricaoTFC, Utilizador
from propostas.models import Proposta
from tfc.models import TFC, TFCAluno

from .models import Candidatura, Grupo


def erro_bd():
    """Erros levantados pelos triggers (RAISE EXCEPTION) e pelas restrições chegam ao Django como DatabaseError."""
    return DatabaseError


class Base(TestCase):
    def setUp(self):
        agora = timezone.now()
        self.ano = AnoLetivo.objects.create(designacao="2099/00", data_referencia_elegibilidade=agora.date())
        Fase.objects.create(ano_letivo=self.ano, tipo="CANDIDATURAS",
                            data_inicio=agora - timedelta(days=1), data_fim=agora + timedelta(days=1))
        self.curso = Curso.objects.get(codigo="LEI")
        u = Utilizador.objects.create(username="docente", email="d@x.pt", nome="Docente")
        self.docente = Docente.objects.create(utilizador=u)
        self.alunos = [self.criar_aluno(i) for i in range(1, 5)]
        self.propostas = [self.criar_proposta(i) for i in range(1, 6)]

    def criar_aluno(self, i, ects=120):
        u = Utilizador.objects.create(username=f"a{i}", email=f"a{i}@x.pt", nome=f"Aluno {i}")
        a = Aluno.objects.create(utilizador=u, numero=f"2200{i}", curso=self.curso)
        InscricaoTFC.objects.create(aluno=a, ano_letivo=self.ano, ects=ects)
        return a

    def criar_proposta(self, i, modalidade="INDIVIDUAL_OU_GRUPO"):
        return Proposta.objects.create(ano_letivo=self.ano, codigo=f"T{i}", titulo=f"TFC {i}", descricao="-",
                                       modalidade=modalidade, estado="DISPONIVEL", tipo_proponente="DOCENTE",
                                       proponente=self.docente.utilizador, orientador_sugerido=self.docente)

    def candidatar(self, aluno, proposta, grupo=None):
        c = Candidatura.objects.create(ano_letivo=self.ano, aluno=aluno, proposta=proposta, grupo=grupo)
        c.refresh_from_db()
        return c

    def lista(self, aluno):
        return list(Candidatura.objects.filter(aluno=aluno, grupo__isnull=True,
                                               estado__in=["ATIVA", "PENDENTE_CONFIRMACAO"])
                    .order_by("prioridade").values_list("proposta__codigo", "prioridade"))


class ListaDeCandidaturasTests(Base):
    def test_candidatura_fica_na_ultima_posicao(self):
        a = self.alunos[0]
        for p in self.propostas[:3]:
            self.candidatar(a, p)
        self.assertEqual(self.lista(a), [("T1", 1), ("T2", 2), ("T3", 3)])

    def test_cancelar_sobe_as_seguintes(self):
        a = self.alunos[0]
        cs = [self.candidatar(a, p) for p in self.propostas[:4]]
        cs[1].estado = "CANCELADA"
        cs[1].save()
        cs[1].refresh_from_db()
        self.assertIsNone(cs[1].prioridade)
        self.assertEqual(self.lista(a), [("T1", 1), ("T3", 2), ("T4", 3)])

    def test_mudar_prioridade(self):
        a = self.alunos[0]
        cs = [self.candidatar(a, p) for p in self.propostas[:4]]
        with connection.cursor() as cur:
            cur.execute("SELECT mover_candidatura(%s, %s)", [cs[3].id, 1])
        self.assertEqual(self.lista(a), [("T4", 1), ("T1", 2), ("T2", 3), ("T3", 4)])

    def test_sem_creditos_fica_recusada(self):
        sem = self.criar_aluno(9, ects=60)
        c = self.candidatar(sem, self.propostas[0])
        self.assertEqual((c.estado, c.motivo_fim, c.prioridade), ("RECUSADA", "SEM_CREDITOS", None))

    def test_limite_de_candidaturas(self):
        self.ano.min_candidaturas, self.ano.max_candidaturas = 1, 2
        self.ano.save()
        a = self.alunos[0]
        self.candidatar(a, self.propostas[0])
        self.candidatar(a, self.propostas[1])
        with self.assertRaises(erro_bd()), transaction.atomic():
            self.candidatar(a, self.propostas[2])

    def test_tfc_de_grupo_nao_aceita_individual(self):
        p = self.criar_proposta(10, modalidade="GRUPO")
        with self.assertRaises(erro_bd()), transaction.atomic():
            self.candidatar(self.alunos[0], p)

    def test_candidatura_repetida(self):
        self.candidatar(self.alunos[0], self.propostas[0])
        with self.assertRaises(erro_bd()), transaction.atomic():
            self.candidatar(self.alunos[0], self.propostas[0])

    def test_fase_fechada(self):
        Fase.objects.filter(ano_letivo=self.ano).update(data_fim=timezone.now() - timedelta(hours=1),
                                                        data_inicio=timezone.now() - timedelta(days=2))
        with self.assertRaises(erro_bd()), transaction.atomic():
            self.candidatar(self.alunos[0], self.propostas[0])

    def test_candidatura_em_grupo_fica_pendente(self):
        g = Grupo.objects.create(ano_letivo=self.ano, submissor=self.alunos[0], colega=self.alunos[1])
        c = self.candidatar(self.alunos[0], self.propostas[0], grupo=g)
        self.assertEqual((c.estado, c.prioridade), ("PENDENTE_CONFIRMACAO", 1))


class AtribuirTFCTests(Base):
    def atribuir(self, candidatura):
        with connection.cursor() as cur:
            cur.execute("SELECT atribuir_tfc(%s, %s)", [candidatura.id, self.docente.id])
            return cur.fetchone()[0]

    def test_atribuicao_desencadeia_as_restantes_operacoes(self):
        a1, a2 = self.alunos[0], self.alunos[1]
        c_a1 = [self.candidatar(a1, p) for p in self.propostas[:3]]   # a1: T1, T2, T3
        c_a2 = [self.candidatar(a2, p) for p in self.propostas[1:4]]  # a2: T2, T3, T4

        tfc_id = self.atribuir(c_a1[1])  # T2 atribuído ao aluno 1

        tfc = TFC.objects.get(id=tfc_id)
        self.assertEqual((tfc.estado, tfc.proposta.estado), ("EM_CURSO", "ATRIBUIDA"))
        self.assertTrue(TFCAluno.objects.filter(tfc=tfc, aluno=a1, ativo=True).exists())
        # Candidatura contemplada e as outras do aluno 1 encerradas
        estados = {c.proposta.codigo: (c.estado, c.motivo_fim)
                   for c in Candidatura.objects.filter(aluno=a1)}
        self.assertEqual(estados, {"T1": ("ENCERRADA", "ALUNO_CONTEMPLADO"), "T2": ("CONTEMPLADA", ""),
                                   "T3": ("ENCERRADA", "ALUNO_CONTEMPLADO")})
        # Aluno 2 perde T2 (atribuído a outro) e a lista sobe
        self.assertEqual(Candidatura.objects.get(id=c_a2[0].id).motivo_fim, "TFC_ATRIBUIDO_A_OUTRO")
        self.assertEqual(self.lista(a2), [("T3", 1), ("T4", 2)])

    def test_nao_atribui_proposta_ja_atribuida(self):
        c1 = self.candidatar(self.alunos[0], self.propostas[0])
        c2 = self.candidatar(self.alunos[1], self.propostas[1])
        self.atribuir(c1)
        Candidatura.objects.filter(id=c2.id).update(proposta=self.propostas[0])
        with self.assertRaises(erro_bd()), transaction.atomic():
            self.atribuir(c2)
