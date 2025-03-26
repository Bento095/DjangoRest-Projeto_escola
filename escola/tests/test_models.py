from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
   # def teste_falha(self):
      #  self.fail('Teste falhou!')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='Teste de Modelo',
            email='testedemodelo@gmail.com',
            cpf='98190389017',
            data_nascimento='2000-01-01',
            celular='42 99999-9999'
        )
        
    def test_verifica_atributos_estudante(self):
            """Teste para verificar os atributos do modelo Estudante"""
            self.assertEqual(self.estudante.nome, 'Teste de Modelo')
            self.assertEqual(self.estudante.email, 'testedemodelo@gmail.com')
            self.assertEqual(self.estudante.cpf, '98190389017')
            self.assertEqual(self.estudante.data_nascimento, '2000-01-01')
            self.assertEqual(self.estudante.celular, '42 99999-9999')

class ModeloCursoTestCase(TestCase):
    #def teste_falha(self):
    #    self.fail('Teste falhou!')
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo='CTT1',
            descricao='Curso de Teste',
            nivel='B'
        )
    
    def test_verifica_atributos_curso(self):
        """Teste para verificar os atributos do modelo Curso"""
        self.assertEqual(self.curso.codigo, 'CTT1')
        self.assertEqual(self.curso.descricao, 'Curso de Teste')
        self.assertEqual(self.curso.nivel, 'B')

class ModeloMatriculaTestCase(TestCase):
    #def teste_falha(self):
    #    self.fail('Teste falhou!')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='Teste de Modelo',
            email='testedemodelo@gmail.com',
            cpf='98190389017',
            data_nascimento='2000-01-01',
            celular='42 99999-9999'
        )
        self.curso = Curso.objects.create(
            codigo='CTT1',
            descricao='Curso de Teste',
            nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='B'
        )
    
    def test_verifica_atributos_matricula(self):
        """Teste para verificar os atributos do modelo Matricula"""
        self.assertEqual(self.matricula.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.matricula.curso.codigo, 'CTT1')
        self.assertEqual(self.matricula.periodo, 'B')