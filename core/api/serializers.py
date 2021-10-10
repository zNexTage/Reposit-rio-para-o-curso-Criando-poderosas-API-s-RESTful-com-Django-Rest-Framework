from rest_framework.fields import ReadOnlyField, SerializerMethodField
from atracoes.models import Atracoes
from core.models import DocIdentificacao, PontoTuristico
from rest_framework import serializers
from atracoes.api.serializer import AtracoesSerializer
from enderecos.api.serializer import EnderecoSerializer
from enderecos.models import Endereco

class DocIdentificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields='__all__'

class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecoSerializer()
    # Executara a função get_descricao_completa
    descricao_completa = SerializerMethodField()
    # Precisa colocar o campo descricao_completa no fields do serializer
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'fotos', 'atracoes',
                  'comentarios', 'avaliacao', 'endereco', 'descricao_completa', 'descricao_completa_2', 'doc_identificacao')
        # descricao_completa_2 foi definido na model;
        # Para campos comuns da model
        read_only_fields = ('comentarios', 'avaliacao')

    def create_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracoes.objects.create(**atracao)
            
            ponto.atracoes.add(at)

    def create(self, validated_data):        
        atracoes = validated_data.pop('atracoes')
        endereco = validated_data.pop('endereco')
        doc = validated_data.pop('doc_identificacao')

        ponto = PontoTuristico.objects.create(**validated_data)
        end = Endereco.objects.create(**endereco)
        doc = DocIdentificacao.objects.create(**doc)

        self.create_atracoes(atracoes, ponto)
        ponto.endereco = end
        ponto.doc_identificacao = doc

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '{} - {}'.format(obj.nome, obj.descricao)
