from django.contrib import admin
from cadastro.models import Editoras, Alunos, Livros, Categorias, Autores

class EditorasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    list_filter = ['cidade']


admin.site.register(Editoras, EditorasAdmin)

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('ra', 'nome', 'email', 'celular', 'cidade')
    list_filter = ['sala']

    class Media:
        js = (
            'js/scripts.js',
        )

admin.site.register(Alunos, AlunosAdmin)

class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'edicao', 'qtd_disponivel')
    list_filter = ['ano']

admin.site.register(Livros, LivrosAdmin)
admin.site.register(Categorias)
admin.site.register(Autores)
