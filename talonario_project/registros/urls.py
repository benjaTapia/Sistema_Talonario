from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import HistorialArchivosEliminadosView

app_name = 'registros'  # Define el namespace de la aplicación

urlpatterns = [

    # Lista de registros (vista principal)
    path('', login_required(views.RegistroListView.as_view()), name='lista_registros'),

    # Crear un nuevo registro
    path('crear/', views.RegistroCreateView.as_view(), name='crear_registro'),

    # Editar un registro existente
    path('<int:pk>/editar/', views.RegistroUpdateView.as_view(), name='editar_registro'),

    # Ver detalle de un registro
    path('<int:pk>/detalle/', views.RegistroDetailView.as_view(), name='detalle_registro'),

    # Exportar registros a Excel
    path('exportar/excel/', views.exportar_excel, name='exportar_excel'),

    # Editar perfil del usuario
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),

    # Adjuntar Firmado
    path('<int:pk>/adjuntar_firmado/', views.adjuntar_firmado, name='adjuntar_firmado'),

    # Generar PDF
    path('<int:pk>/generar-pdf/', views.generar_pdf, name='generar_pdf'),

    # Archivos Eliminados
    path('historial-archivos/', HistorialArchivosEliminadosView.as_view(), name='historial-archivos'),

    # Libro de Contabilidad
    path('contabilidad/', views.contabilidad_view, name='contabilidad'),

    # Exportar registros de contabilidad a Excel
    path('exportar-excel-contabilidad/', views.exportar_excel_contabilidad, name='exportar_excel_contabilidad'),

    # Exportar registros de contabilidad a PDF
    path('exportar-pdf-contabilidad/', views.exportar_pdf_contabilidad, name='exportar_pdf_contabilidad'),

    # Eliminar registros
    path('registro/<int:pk>/eliminar/', views.RegistroDeleteView.as_view(), name='eliminar_registro'),
]

from django.conf.urls import handler404, handler500
from registros.views import error_404_view, error_500_view  # Importa las vistas

handler404 = 'registros.views.error_404_view'
handler500 = 'registros.views.error_500_view'
