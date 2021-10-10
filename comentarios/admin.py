from django.contrib import admin
from .models import Comentarios
from .actions import reprova_comentarios, aprova_comentarios

class ComentarioAdmin(admin.ModelAdmin):
    list_display=['usuario', 'data', 'aprovado']
    actions = [reprova_comentarios, aprova_comentarios]

# Register your models here.
admin.site.register(Comentarios, ComentarioAdmin)



