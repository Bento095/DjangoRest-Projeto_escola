#operações CRUD, ler , deletar, criar, editar...

from escola.models import Estudante,Curso,Matricula #objetos dos modelos
from escola.serializers import EstudanteSerializer, CursoSerializer,MatriculaSerializer,ListaMatriculaEstudanteSerializer,ListaMatriculaCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Um viewset para visualizar e editar instâncias de Estudante.

    Atributos:
        queryset: Um queryset contendo todas as instâncias de Estudante ordenadas por 'id'.
        filter_backends: Uma lista de backends de filtro usados para filtrar o queryset.
        ordering_fields: Uma lista de campos que podem ser usados para ordenar o queryset.
        search_fields: Uma lista de campos que podem ser usados para pesquisar no queryset.

    Métodos:
        get_serializer_class(self):
            Retorna a classe de serializer apropriada com base na versão da requisição.
    """
    #queryset com as instancias do modelo
    queryset = Estudante.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """
    Um viewset para visualizar e editar instâncias de Curso.

    Atributos:
        queryset: Um queryset contendo todas as instâncias de Curso ordenadas por 'id'.
        serializer_class: A classe de serializer usada para serializar as instâncias de Curso.
    """
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #limitar acesso

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Um viewset para visualizar e editar instâncias de Matricula.

    Atributos:
        queryset: Um queryset contendo todas as instâncias de Matricula ordenadas por 'id'.
        serializer_class: A classe de serializer usada para serializar as instâncias de Matricula.
        throttle_classes: Uma lista de classes de throttle usadas para limitar as requisições.
        http_method_names: Uma lista de métodos HTTP permitidos para esta view.
    """
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle] #limitar requisições
    http_method_names = ["get", "post"] #limitar metodos


class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculaEstudanteSerializer 
    #ir para urls criar a rota

class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculaCursoSerializer
