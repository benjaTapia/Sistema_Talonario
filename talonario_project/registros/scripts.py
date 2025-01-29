from celery import shared_task
from registros.models import Registro

@shared_task
def limpiar_registros_invalidos():
    registros_invalidos = Registro.objects.filter(folio__isnull=True) | Registro.objects.filter(folio='')
    cantidad = registros_invalidos.count()
    registros_invalidos.delete()
    return f"Registros eliminados automáticamente: {cantidad}"
