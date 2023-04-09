from django.contrib import admin
from django.utils.html import format_html

from cadastro.models import Alunos, Livros, Categorias

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('ra', 'nome', 'email', 'celular', 'cidade')
    list_filter = ['sala']

    class Media:
        js = (
            'js/script_cep.js',
        )

admin.site.register(Alunos, AlunosAdmin)

class LivrosAdmin(admin.ModelAdmin):
    fields = ['isbn', 'titulo', 'ano', 'edicao', 'qtd_disponivel', 'autor', 'editora', 'categoria', 'destaque', 'imagem', 'descricao']
    list_display = ('titulo', 'ano', 'edicao', 'qtd_disponivel', 'destaque')
    list_filter = ['ano']

    class Media:
        js = (
            'js/script_isbn.js',
        )

admin.site.register(Livros, LivrosAdmin)

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nome')

admin.site.register(Categorias)