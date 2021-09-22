from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentarios

class ComentariosSerializer(ModelSerializer):
    class Meta:
        model =Comentarios
        fields=('id', 'usuario', 'comentario', 'data', 'aprovado')