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

class Editoras(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Editoras'

    def __str__(self):
        return self.nome


class Autores(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome

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
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editoras, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autores, related_name='livros')
    imagem = models.ImageField(upload_to='livros/')
    destaque = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.titulo

class LivrosAutores(models.Model):
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Livros Autores'

    def __str__(self):
        return f"{self.livro.titulo} - {self.autor.nome}"
