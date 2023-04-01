from django.contrib import admin
from .models import Livros

class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'edicao', 'qtd_disponivel')  # Adiciona as colunas 'titulo', 'ano', 'edicao' e 'qtd_disponivel' na lista de exibição
    list_filter = ['ano']  # Adiciona 'cidade' na lista de filtros

admin.site.register(Livros, LivrosAdmin)