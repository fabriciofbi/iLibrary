import os

from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models.functions import Substr
from .models import Livros


def index(request):
    context = {
        'livros': Livros.objects.filter(destaque=True).distinct()
    }
    return render(request, 'index.html', context)

class IndexListView(ListView):
    template_name = 'index.html'
    model = Livros
    paginate_by = 12
    ordering = 'id'

def livros(request):
    return render(request, 'livros.html')

def autores(request):
    autores = Livros.objects.order_by('autor').distinct().values_list('autor', flat=True)

    context = {
        'autores': autores
    }

    return render(request, 'autores.html', context)

def editoras(request):
    editoras = Livros.objects.order_by('editora').distinct().values_list('editora', flat=True)

    context = {
        'editoras': editoras
    }

    return render(request, 'editoras.html', context)


def categorias(request):
    return render(request, 'categorias.html')

def contato(request):
    return render(request, 'contato.html')

def teste(request):
    return render(request, 'teste.html')

def busca(request):
    return render(request, 'busca.html')

def favicon_view(request):
    # Caminho completo para o arquivo "favicon.ico"
    favicon_path = os.path.join(os.path.dirname(__file__), '..', 'favicon.ico')
    with open(favicon_path, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/x-icon')

