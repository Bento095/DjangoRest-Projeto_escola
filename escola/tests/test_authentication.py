from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')

    def test_autenticacao_user_credenciais_corretas(self):
        '''Teste para verificar se o usuário é autenticado com credenciais corretas'''
        user = authenticate(username='admin', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_autenticacao_username_incorreto(self):
        '''Teste para verificar se o usuário é autenticado com username incorreto'''
        user = authenticate(username='bola', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated)


    def test_autenticacao_user_senhas_incorreta(self):
        '''Teste para verificar se o usuário é autenticado com senha incorreta'''
        user = authenticate(username='admin', password='bola')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_autorizada(self):
        '''Teste para verificar se a requisição GET é autorizada'''
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_requisicao_get_nao_autorizada(self):
        '''Teste para verificar se a requisição GET não é autorizada'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)