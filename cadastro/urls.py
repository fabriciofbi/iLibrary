from django.urls import path

from .views import index, teste, autores

urlpatterns = [
    path('', index, name='index'),
    path('teste/', teste, name='teste'),
    path('autores/', autores, name='autores'),
]