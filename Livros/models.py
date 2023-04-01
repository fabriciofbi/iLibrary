from django.db import models

# Create your models here.
class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField(max_length=4)
    edicao = models.IntegerField(max_length=2)
    qtd_disponivel = models.IntegerField(max_length=5)
    data_cadastro = models.DateTimeField()