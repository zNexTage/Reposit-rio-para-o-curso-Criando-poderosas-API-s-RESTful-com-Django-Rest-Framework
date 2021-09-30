from core.models import PontoTuristico
from rest_framework import serializers
from core.models import PontoTuristico

class PontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields=('id', 'nome', 'descricao', 'aprovado', 'fotos')

