from django.db import models

# Create your models here.
class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    edicao = models.IntegerField()
    qtd_disponivel = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Livro'