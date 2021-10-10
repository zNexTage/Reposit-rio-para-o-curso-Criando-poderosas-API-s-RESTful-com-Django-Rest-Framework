from rest_framework.fields import ReadOnlyField, SerializerMethodField
from atracoes.models import Atracoes
from core.models import PontoTuristico
from rest_framework import serializers
from atracoes.api.serializer import AtracoesSerializer
from enderecos.api.serializer import EnderecoSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecoSerializer(read_only=True)
    # Executara a função get_descricao_completa
    descricao_completa = SerializerMethodField()
    # Precisa colocar o campo descricao_completa no fields do serializer

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'fotos', 'atracoes',
                  'comentarios', 'avaliacao', 'endereco', 'descricao_completa', 'descricao_completa_2')
        # descricao_completa_2 foi definido na model;
        # Para campos comuns da model
        read_only_fields = ('comentarios', 'avaliacao')

    def create_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracoes.objects.create(**atracao)
            
            ponto.atracoes.add(at)

    def create(self, validated_data):
        print(validated_data)
        atracoes = validated_data.pop('atracoes')

        ponto = PontoTuristico.objects.create(**validated_data)

        self.create_atracoes(atracoes, ponto)

        return ponto

    def get_descricao_completa(self, obj):
        return '{} - {}'.format(obj.nome, obj.descricao)
