from django.db import models

# Create your models here.
class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Aluno'