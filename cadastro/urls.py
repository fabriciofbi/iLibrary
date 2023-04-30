from django.urls import path, include
from rest_framework import routers

from . import views
from .views import livros, autores, editoras, categorias, contato, favicon_view, busca, IndexListView, equipe, teste, AlunosViewSet, LivrosViewSet, EditorasViewSet, AutoresViewSet, CategoriasViewSet

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet)
router.register('livros', LivrosViewSet)
router.register('autores', AutoresViewSet)
router.register('editoras', EditorasViewSet)
router.register('categorias', CategoriasViewSet)
urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('livros/', livros, name='livros'),
    path('autores/', autores, name='autores'),
    path('editoras/', editoras, name='editoras'),
    path('categorias/', categorias, name='categorias'),
    path('contato/', contato, name='contato'),
    path('equipe/', equipe, name='equipe'),
    path('busca/', busca, name='busca'),
    path('teste/', teste, name='teste'),
    path('favicon.ico', favicon_view, name='favicon'),
    path('api/', include(router.urls)),
    path('autor/<int:id>/', views.livros_por_autor, name='livros_por_autor'),
    path('editora/<int:id>/', views.livros_por_editora, name='livros_por_editora'),
    path('categoria/<int:id>/', views.livros_por_categoria, name='livros_por_categoria'),
    path('livro/<int:id>/', views.livro, name='livro'),
]