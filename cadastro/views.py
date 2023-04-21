import os

from django.http import HttpResponse
from django.shortcuts import render
from django.db.models.functions import Substr

from .models import Livros
from .models import Categorias

# Create your views here.
def index(request):
    context = {
        'livros': Livros.objects.filter(destaque=True)[:24]
    }
    return render(request, 'index.html', context)

def livros(request):
    return render(request, 'livros.html')

def autores(request):
    def lista_letras_com_autores():
        letras = Livros.objects.annotate(primeira_letra=Substr('autor',1,1)).values('primeira_letra').distinct().order_by('primeira_letra')
        return letras

    def lista_autores_por_letra(letra):
        autores = Livros.objects.filter(autor__startswith=letra).order_by('autor')
        return autores

    def todos_os_autores(letra):
        todos_autores = Livros.objects.all()
        return todos_autores


    letras_com_autores = lista_letras_com_autores()
    autores = []
    todos_os_autores = []
    for letra in letras_com_autores:
        autores_por_letra = lista_autores_por_letra(letra['primeira_letra'])
        autores.append({'letra': letra['primeira_letra'], 'autores': autores_por_letra})

    context = {'letras_com_autores': letras_com_autores, 'autores': autores, 'todos_os_autores': todos_os_autores}

    return render(request, 'autores.html', context)

def editoras(request):
    def lista_letras_com_editoras():
        letras = Livros.objects.annotate(primeira_letra=Substr('editora',1,1)).values('primeira_letra').distinct().order_by('primeira_letra')
        return letras

    def lista_editoras_por_letra(letra):
        editoras = Livros.objects.filter(editora__startswith=letra).order_by('editora')
        return editoras

    def todas_as_editoras(letra):
        todas_editoras = Livros.objects.all()
        return todas_editoras


    letras_com_editoras = lista_letras_com_editoras()
    editoras = []
    todas_as_editoras = []
    for letra in letras_com_editoras:
        editoras_por_letra = lista_editoras_por_letra(letra['primeira_letra'])
        editoras.append({'letra': letra['primeira_letra'], 'editoras': editoras_por_letra})

    context = {'letras_com_editoras': letras_com_editoras, 'editoras': editoras, 'todas_as_editoras': todas_as_editoras}

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