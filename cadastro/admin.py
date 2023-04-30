from django.contrib import admin
from django.utils.html import format_html

from cadastro.models import Alunos, Livros, Categorias, Editoras, Autores

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('ra', 'nome', 'email', 'celular', 'cidade')
    list_filter = ['sala']
    search_fields = ['ra', 'nome']

    class Media:
        js = (
            'js/script_cep.js',
        )

admin.site.register(Alunos, AlunosAdmin)

class EditorasAdmin(admin.ModelAdmin):
    fields = ["nome"]
    search_fields = ('id', 'nome')

admin.site.register(Editoras, EditorasAdmin)

class AutoresAdmin(admin.ModelAdmin):
    fields = ["nome"]
    search_fields = ('id', 'nome')
    ordering = ['nome']

admin.site.register(Autores, AutoresAdmin)

class LivrosAdmin(admin.ModelAdmin):
    fields = ['isbn', 'titulo', 'ano', 'edicao', 'qtd_disponivel', 'categoria', 'autores', 'editora', 'destaque', 'imagem', 'descricao']
    list_display = ('titulo', 'ano', 'edicao', 'qtd_disponivel', 'destaque')
    list_filter = ['ano']
    search_fields = ['isbn', 'titulo']

    class Media:
        js = (
            'js/script_isbn.js',
        )

admin.site.register(Livros, LivrosAdmin)

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nome')

admin.site.register(Categorias)