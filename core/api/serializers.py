from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from rest_framework import serializers
from atracoes.api.serializer import AtracoesSerializer
from enderecos.api.serializer import EnderecoSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField() #Executara a função get_descricao_completa
    # Precisa colocar o campo descricao_completa no fields do serializer
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'fotos', 'atracoes',
                  'comentarios', 'avaliacao', 'endereco', 'descricao_completa','descricao_completa_2') 
        #descricao_completa_2 foi definido na model;

    


    def get_descricao_completa(self, obj):
        return '{} - {}'.format(obj.nome, obj.descricao)
