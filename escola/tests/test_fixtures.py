from django.test import TestCase
from escola.models import Estudante, Curso

class fixturesTestCase(TestCase):
    fixures = ['prototipo_banco.json']

    def text_carregamento_fixtures(self):
        '''teste que verifica o carregamento da fixtures'''
        estudante = Estudante.objects.get(cpf='66612384695')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular, '42 99999-8888')
        self.assertEqual(curso.codigo, 'RBOL')