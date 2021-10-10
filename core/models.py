from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

# Create your models here.

class DocIdentificacao(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.descricao

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracoes)
    comentarios = models.ManyToManyField(Comentarios)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)
    fotos = models.ImageField(
        upload_to='pontos_turisticos', null=True, blank=True)
    doc_identificacao = models.OneToOneField(DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True)
    
    #Pode ser usado no serializer
    @property
    def descricao_completa_2(self):
        return '{} - {} (Model)'.format(self.nome, self.descricao)

    def __str__(self):
        return self.nome
