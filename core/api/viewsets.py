from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    # queryset=PontoTuristico.objects.all()
    serializer_class=PontoTuristicoSerializer
    # http_method_names=['DELETE', ] # Quais requisições http a nossa api aceita


    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
        
    # Override das funções padrões da Viewset
    # O objeto request retorna diversas informações, por exemplo: usuário logado, paramêtros e etc...

    #GET
    def list(self, request, *args, **kwargs):
        # return Response({'teste': 123})
        return super().list(request, *args, **kwargs)
    
    #POST
    def create(self, request, *args, **kwargs):
        # return Response({'teste': 123})
        return super().create(request, *args, **kwargs)

    #DELETE
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    #GET em um recurso do endpoint.
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    #PUT
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    #PATCH
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        ponto = PontoTuristico.objects.filter(pk=pk).first()

        if not ponto:
            return Response({'message': 'Esse ponto turistico não existe'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'O ponto de turistico {} foi denunciado com sucesso'.format(ponto.nome)})