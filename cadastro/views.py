import os

from django.http import HttpResponse
from django.shortcuts import render

from .models import Livros

# Create your views here.
def index(request):
    context = {
        'livros': Livros.objects.filter(destaque=True)[:24]
    }
    return render(request, 'index.html', context)

def livros(request):
    return render(request, 'livros.html')

def autores(request):
    return render(request, 'autores.html')

def editoras(request):
    return render(request, 'editoras.html')

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