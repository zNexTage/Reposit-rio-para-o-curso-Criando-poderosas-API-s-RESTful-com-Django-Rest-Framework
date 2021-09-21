from django.db import models

# Create your models here.
class Atracoes(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nome
    