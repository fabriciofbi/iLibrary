from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def teste(request):
    return render(request, 'teste.html')

def autores(request):
    return render(request, 'autores.html')

