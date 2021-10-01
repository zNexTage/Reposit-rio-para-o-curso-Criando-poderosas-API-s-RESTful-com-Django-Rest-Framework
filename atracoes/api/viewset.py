from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracoes
from .serializer import AtracoesSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class AtracoesViewSet(ModelViewSet):
    queryset = Atracoes.objects.all()
    serializer_class = AtracoesSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('nome', 'descricao')

