from rest_framework import fields
from atracoes.models import Atracoes
from rest_framework.serializers import ModelSerializer


class AtracoesSerializer(ModelSerializer):
    class Meta:
        model = Atracoes
        fields = ('id' ,'nome', 'descricao', 'horario_func', 'idade_minima', 'fotos', 'observacoes')
    