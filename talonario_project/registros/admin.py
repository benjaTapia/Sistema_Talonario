from django.contrib import admin
from .models import Registro, ArchivoAdjunto

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('folio', 'nombre_registro', 'tipo_registro', 'fecha_creacion', 'monto')
    search_fields = ('folio', 'nombre_registro', 'tipo_registro')
    list_filter = ('tipo_registro', 'fecha_creacion')

@admin.register(ArchivoAdjunto)
class ArchivoAdjuntoAdmin(admin.ModelAdmin):
    list_display = ('registro', 'descripcion', 'archivo')
    search_fields = ('registro__folio', 'descripcion')
