from django.contrib import admin

from .models import Devolucao
from locacao.models import Locacao
from django.contrib import admin

class DevolucaoAdmin(admin.ModelAdmin):
    list_display = ('locacao', 'data_devolucao')
    autocomplete_fields = ['locacao']

    def save_model(self, request, obj, form, change):
        obj.locacao.save()
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "locacao":
            kwargs["queryset"] = Locacao.objects.filter(devolvido=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Devolucao, DevolucaoAdmin)
