from os import path

from django.db import models
from django.core.exceptions import ValidationError
from cpf_field.models import CPFField
from django.http import HttpResponse
from validate_email import validate_email
from django.core.validators import MinValueValidator


class Alunos(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    ra = models.IntegerField(unique=True)
    cpf = CPFField(error_messages={'invalid': 'CPF inválido'}, unique=True, blank=True, max_length=11)
    cep = models.CharField(max_length=8, blank=True)
    endereco = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    celular = models.CharField(max_length=12, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    sala = models.CharField(max_length=10, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Aluno'

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def clean(self):
        if self.email and not validate_email(self.email):
            raise ValidationError('Endereço de email inválido.')

class Categorias(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Livros(models.Model):
    isbn = models.CharField(max_length=16, unique=True)
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField(validators=[MinValueValidator(1)])
    edicao = models.IntegerField()
    qtd_disponivel = models.IntegerField()
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='livros/')
    destaque = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.titulo

