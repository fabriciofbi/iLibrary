from django.urls import path

from .views import livros, autores, editoras, categorias, contato, favicon_view, busca, IndexListView, equipe

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('livros/', livros, name='livros'),
    path('autores/', autores, name='autores'),
    path('editoras/', editoras, name='editoras'),
    path('categorias/', categorias, name='categorias'),
    path('contato/', contato, name='contato'),
    path('equipe/', equipe, name='equipe'),
    path('busca/', busca, name='busca.html'),
    path('favicon.ico', favicon_view, name='favicon'),
]