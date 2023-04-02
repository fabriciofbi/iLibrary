from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from Editoras.models import Editoras

class Categorias(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField(validators=[MinValueValidator(1)])
    edicao = models.IntegerField()
    qtd_disponivel = models.IntegerField()
    editora = models.ForeignKey(Editoras, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=16, unique=True)
    imagem = models.ImageField(upload_to='livros/img/', blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Livro'

