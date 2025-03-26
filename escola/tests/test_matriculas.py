from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Matricula, Estudante, Curso
from escola.serializers import MatriculaSerializer

class MatriculasTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='Bento')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudante.objects.get(pk=1)
        self.curso = Curso.objects.get(pk=1)
        self.matricula = Matricula.objects.get(pk=1)

    def test_get_para_listar_matriculas(self):
        """Testa requisição GET para listar matrículas"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_para_listar_uma_matricula(self):
        """Testa requisição GET para uma matrícula"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_matricula = Matricula.objects.get(pk=1)
        dados_matricula_serializados = MatriculaSerializer(instance=dados_matricula).data
        self.assertEqual(response.data, dados_matricula_serializados)

    def test_requisicao_post_para_criar_uma_matricula(self):
        """Testa requisição POST para uma matrícula"""
        dados = {
            'estudante':self.estudante.pk,
            'curso':self.curso.pk,
            'periodo':'M'
        }
        response = self.client.post(self.url,dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       
    def test_requisicao_delete_uma_matricula(self):
        """Teste requisição delete uma matricula"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_uma_matricula(self):
        """Testa requisição PUT para atualizar uma matrícula"""
        dados = {
            'estudante':self.estudante.pk,
            'curso':self.curso.pk,
            'periodo':'M'
        }
        response = self.client.put(f'{self.url}1/',dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        