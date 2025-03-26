from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    
    def setUp(self):
        self.usuario = User.objects.get(username='Bento')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.get(pk=1)
        self.curso_02 = Curso.objects.get(pk=2)

    def test_get_para_listar_cursos(self):
        """Testa requisição GET para listar cursos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_para_listar_um_curso(self):
        """Testa requisição GET para um curso"""
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data, dados_curso_serializados)

    def test_requisicao_post_para_criar_um_curso(self):
        """Testa requisição POST para um curso"""
        dados = {
            'codigo': 'CTT3',
            'descricao': 'Curso Teste 3',
            'nivel': 'A',
        }
        # Verifica o número de cursos antes da requisição POST
        cursos_antes = Curso.objects.count()
        
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verifica o número de cursos após a requisição POST
        cursos_depois = Curso.objects.count()
        self.assertEqual(cursos_depois, cursos_antes + 1)
        
        # Verifica se o curso criado tem os dados corretos
        curso_criado = Curso.objects.get(codigo='CTT3')
        self.assertEqual(curso_criado.descricao, 'Curso Teste 3')

    def test_requisicao_delete_um_curso(self):
        """Teste requisição delete um curso"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_curso(self):
        """Testa requisição PUT para atualizar um curso"""
        dados = {
            'codigo': 'CTT2',
            'descricao': 'Curso Teste 2 Atualizado',
            'nivel': 'B',
        }
        response = self.client.put(f'{self.url}2/', dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)