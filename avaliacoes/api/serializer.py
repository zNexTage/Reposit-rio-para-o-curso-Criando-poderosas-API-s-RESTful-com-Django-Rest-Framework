from django.db import models
from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'usuario', 'comentarios', 'nota', 'data')
