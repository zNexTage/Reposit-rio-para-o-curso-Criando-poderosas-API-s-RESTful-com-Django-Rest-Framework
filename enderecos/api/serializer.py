from enderecos.models import Endereco
from django.db import models
from rest_framework.serializers import ModelSerializer


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields=(
            'id', 'linha1', 'linha2', 'cidade', 'estado', 
            'pais', 'latitude', 'longitude')