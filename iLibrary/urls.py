from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro.urls')),
]

admin.AdminSite.site_header = 'iLibrary - Administração'
admin.AdminSite.site_title = 'iLibrary - Administração'
admin.AdminSite.index_title = 'Gestão de Bibliotecas'
