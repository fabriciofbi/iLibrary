import os

from django.views.generic import ListView
from django.http import HttpResponse
from .models import Livros, Categorias, Alunos, Autores, Editoras
from .forms import ContatoForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import AlunosSerializer, LivrosSerializer, EditorasSerializer, AutoresSerializer, CategoriasSerializer

def index(request):
    context = {
        'livros': Livros.objects.filter(destaque=True)
    }
    return render(request, 'index.html', context)

class IndexListView(ListView):
    template_name = 'index.html'
    model = Livros
    paginate_by = 12
    ordering = 'id'

def livros(request):
    livros = Livros.objects.all()

    context = {
        'livros': livros
    }

    return render(request, 'livros.html', context)

def autores(request):
    autores = Autores.objects.all().order_by('nome')

    context = {
        'autores': autores
    }

    return render(request, 'autores.html', context)

def livros_por_autor(request, id):
    autor = Autores.objects.get(id=id)
    livros = Livros.objects.filter(autores=autor)

    context = {
        'autor': autor,
        'livros': livros
    }

    return render(request, 'autor.html', context)

def livros_por_editora(request, id):
    editora = Editoras.objects.get(id=id)
    livros = Livros.objects.filter(editora=editora)

    context = {
        'editora': editora,
        'livros': livros
    }

    return render(request, 'editora.html', context)

def livro(request, id):
    livro = Livros.objects.get(id=id)

    context = {
        'livro': livro
    }

    return render(request, 'livro.html', context)

def livros_por_categoria(request, id):
    categoria = Categorias.objects.get(id=id)
    livros = Livros.objects.filter(categoria=categoria)

    context = {
        'categoria': categoria,
        'livros': livros
    }

    return render(request, 'categoria.html', context)

def editoras(request):
    editoras = Editoras.objects.all()

    context = {
        'editoras': editoras
    }

    return render(request, 'editoras.html', context)


def categorias(request):
    categorias = Categorias.objects.all()

    context = {
        'categorias': categorias
    }

    return render(request, 'categorias.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem Enviada')
            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            # Mostrar mensagem de sucesso
            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContatoForm()
    else:
        messages.error(request, 'Erro ao Enviar Mensagem!')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def busca(request):
    query = request.GET.get('busca')
    livros = Livros.objects.filter(
        Q(titulo__icontains=query) |
        Q(categoria__nome__icontains=query) |
        Q(editora__nome__icontains=query) |
        Q(autores__nome__icontains=query)
    ).distinct()

    context = {
        'livros': livros,
        'busca': query,
    }

    return render(request, 'busca.html', context)

def equipe(request):
    return render(request, 'equipe.html')

def favicon_view(request):
    # Caminho completo para o arquivo "favicon.ico"
    favicon_path = os.path.join(os.path.dirname(__file__), '..', 'favicon.ico')
    with open(favicon_path, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/x-icon')

def teste(request):
    return render(request, 'teste.html')

#Criando View para a API
class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EditorasViewSet(viewsets.ModelViewSet):
    queryset = Editoras.objects.all()
    serializer_class = EditorasSerializer

class AutoresViewSet(viewsets.ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer