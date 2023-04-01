from django.db import models

# Create your models here.
class Alunos(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    endereco = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    celular = models.CharField(max_length=12, blank=True)
    email = models.CharField(max_length=100, blank=True)
    sala = models.CharField(max_length=10, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Aluno'

    def __str__(self):
        return self.nome