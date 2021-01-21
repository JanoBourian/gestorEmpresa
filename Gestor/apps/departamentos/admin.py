from django.contrib import admin
from .models import Departamento

# Register your models here.


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_corto', 'estado', 'fecha', 'usuario')
    list_filter = ('nombre', 'nombre_corto', 'estado', 'fecha', 'usuario')
    search_fields = list_display = (
        'nombre', 'nombre_corto', 'estado', 'fecha', 'usuario')
    # Permite una búsqueda en lugar de desplegar muchos nombres en una lista
    raw_id_fields = ('usuario',)
    date_hierarchy = 'fecha'
    ordering = ('nombre', 'nombre_corto', 'estado')
