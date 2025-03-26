from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome='Teste de Modelo',
            email='testedemodelo@gmail.com',
            cpf='98190389017',
            data_nascimento='2000-01-01',
            celular='42 99999-9999'
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializados_de_estudante(self):
        """Teste para verificar os campos serializados de Estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()), set(['id','nome','email','cpf','data_nascimento','celular']))

    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        """Teste para verificar o conteudo dos campos serializados de Estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(dados['nome'],self.estudante.nome)
        self.assertEqual(dados['email'],self.estudante.email)
        self.assertEqual(dados['cpf'],self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'],self.estudante.data_nascimento)
        self.assertEqual(dados['celular'],self.estudante.celular)

class SerializerCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo='CTT1',
            descricao='Curso de Teste',
            nivel='B'
        )
        self.serializer_curso = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializados_de_curso(self):
        """Teste para verificar os campos serializados de Curso"""
        dados = self.serializer_curso.data
        self.assertEqual(set(dados.keys()), set(['id','codigo','descricao','nivel']))

    def test_verifica_conteudo_dos_campos_serializados_de_curso(self):
        """Teste para verificar o conteudo dos campos serializados de Curso"""
        dados = self.serializer_curso.data
        self.assertEqual(dados['codigo'],self.curso.codigo)
        self.assertEqual(dados['descricao'],self.curso.descricao)
        self.assertEqual(dados['nivel'],self.curso.nivel)

class SerializerMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome='Teste de Modelo',
            email='testedemodelo@gmail.com',
            cpf='98190389017',
            data_nascimento='2000-01-01',
            celular='42 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTT1',
            descricao='Curso de Teste',
            nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='B'
        )
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)

    def test_verifica_campos_serializados_de_matricula(self):
        """Teste para verificar os campos serializados de Matricula"""
        dados = self.serializer_matricula.data
        self.assertEqual(set(dados.keys()), set(['id','estudante','curso','periodo']))

    def test_verifica_conteudo_dos_campos_serializados_de_matricula(self):
        """Teste para verificar o conteudo dos campos serializados de Matricula"""
        dados = self.serializer_matricula.data
        self.assertEqual(dados['estudante'],self.matricula.estudante.id)
        self.assertEqual(dados['curso'],self.matricula.curso.id)
        self.assertEqual(dados['periodo'],self.matricula.periodo)