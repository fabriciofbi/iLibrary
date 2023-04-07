from django.urls import path

from .views import index, teste

urlpatterns = [
    path('', index, name='index'),
    path('teste/', teste, name='teste'),
]