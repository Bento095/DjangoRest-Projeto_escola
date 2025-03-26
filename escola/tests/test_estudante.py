from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        # Cria um usuário superusuário para autenticação nos testes
        #self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.usuario = User.objects.get(username='Bento')
        # Define a URL para a lista de estudantes
        self.url = reverse('Estudantes-list')
        
        # Autentica o cliente de teste com o superusuário criado
        self.client.force_authenticate(user=self.usuario)
        
        # Cria dois estudantes para serem usados nos testes
        # self.estudante_01 = Estudante.objects.create(
        #     nome='Teste Estudante Um',
        #     email='testeestudante01@gmail.com',
        #     cpf='21323511040',  # CPF válido
        #     data_nascimento='2000-01-01',
        #     celular='42 00000-0000'
        # )
        self.estudante_01 = Estudante.objects.get(pk=1)

        # self.estudante_02 = Estudante.objects.create(
        #     nome='Teste Estudante Dois',
        #     email='testeestudante02@gmail.com',
        #     cpf='25797282011',  # CPF válido
        #     data_nascimento='2000-01-01',
        #     celular='42 00000-0000'
        # )
        self.estudante_02 = Estudante.objects.get(pk=2)
        
    def test_get_para_listar_estudantes(self):
        """Teste requisição GET para listar estudantes"""
        # Faz uma requisição GET para a URL definida
        response = self.client.get(self.url)
        
        # Verifica se o status da resposta é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_para_listar_um_estudante(self):
        """Teste requisição GET para um estudante """
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        print(dados_estudante_serializados)
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_para_criar_um_estudante(self):
        """Teste requisição POST para um estudante"""
        dados = {
            'nome':'Teste',
            'email':'teste@gmail.com',
            'cpf':'24688297009',
            'data_nascimento':'2000-01-01',
            'celular':'42 00000-0000'
        }
        response = self.client.post(self.url,data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_estudante(self):
        """Teste requisição delete um estudante"""
        response = self.client.delete(f'{self.url}2/')#/estudantes/2/  
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_estudante(self):
        """Teste requisição PUT para um estudante"""
        dados = {
            'nome':'Teste',
            'email':'testput@gmail.com',
            'cpf':'64011004006',
            'data_nascimento':'2001-01-01',
            'celular':'42 00000-0000'
        }
        response = self.client.put(f'{self.url}1/',data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
