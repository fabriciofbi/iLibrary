from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro.urls')),
    path('', include('locacao.urls')),
    path('', include('devolucao.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.AdminSite.site_header = 'iLibrary - Administração'
admin.AdminSite.site_title = 'iLibrary - Administração'
admin.AdminSite.index_title = 'Gestão de Bibliotecas'
