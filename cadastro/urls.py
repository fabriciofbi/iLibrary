from django.urls import path

from .views import index, livros, autores, editoras, categorias, contato, teste

urlpatterns = [
    path('', index, name='index'),
    path('livros/', livros, name='livros'),
    path('autores/', autores, name='autores'),
    path('editoras/', editoras, name='editoras'),
    path('categorias/', categorias, name='categorias'),
    path('contato/', contato, name='contato'),
    path('teste/', teste, name='teste'),
]