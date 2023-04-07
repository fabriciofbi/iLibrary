from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

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