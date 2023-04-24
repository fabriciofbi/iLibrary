from django.contrib import admin
from django.utils.html import format_html

from .models import Locacao

class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'livro', 'data_locacao', 'data_devolucao', 'devolvido')
    list_filter = ['devolvido']
    autocomplete_fields = ['aluno', 'livro']
    search_fields = ['aluno', 'livro']

admin.site.register(Locacao, LocacaoAdmin)