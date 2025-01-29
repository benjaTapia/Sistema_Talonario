from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.db import models, transaction
import logging
from django.db import IntegrityError
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


# Lista de bancos de Santiago de Chile
BANCOS_CHILE = [
    ('No Especificado', 'No Especificado'),
    ('Banco de Chile', 'Banco de Chile'),
    ('BancoEstado', 'BancoEstado'),
    ('Banco Santander', 'Banco Santander'),
    ('Banco BCI', 'Banco BCI'),
    ('Banco Itaú', 'Banco Itaú'),
    ('Scotiabank Chile', 'Scotiabank Chile'),
    ('Banco Ripley', 'Banco Ripley'),
    ('Banco Falabella', 'Banco Falabella'),
    ('Banco Security', 'Banco Security'),
]

class Registro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registros")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre_registro = models.CharField(max_length=255)
    concepto = models.TextField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    cheque_numero = models.CharField(max_length=100, blank=True, null=True)
    documento_firmado = models.FileField(
        upload_to='documentos_firmados/',
        blank=True,
        null=True,
        verbose_name="Documento Firmado"
    )
    banco = models.CharField(
        max_length=50,
        choices=BANCOS_CHILE,
        blank=True,
        null=True
    )
    detalle = models.TextField(blank=True, null=True)
    tipo_registro = models.CharField(
        max_length=50,
        choices=[
            ('convenio_ingreso', 'Convenio Ingreso'),
            ('convenio_egreso', 'Convenio Egreso'),
            ('aporte_ingreso', 'Aporte Ingreso'),
            ('aporte_egreso', 'Aporte Egreso')
        ],
    )
    folio = models.CharField(max_length=50, unique=True, blank=True)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not self.folio:
            # Mapear tipo_registro a prefijos
            tipo_prefijo = {
                'convenio_ingreso': 'CON-ING',
                'convenio_egreso': 'CON-EGR',
                'aporte_ingreso': 'APO-ING',
                'aporte_egreso': 'APO-EGR',
            }

            # Obtener el prefijo correspondiente
            prefijo = tipo_prefijo.get(self.tipo_registro, 'UNK')  # 'UNK' si no se encuentra el tipo

            # Obtener el año actual
            año_actual = now().year

            # Obtener el último folio para este usuario, tipo y año
            with transaction.atomic():
                ultimo_folio = Registro.objects.filter(
                    usuario=self.usuario,  # Filtrar por usuario actual
                    tipo_registro=self.tipo_registro,  # Filtrar por tipo exacto
                    folio__startswith=prefijo,  # Filtrar por prefijo
                    folio__endswith=f"/{año_actual}"  # Filtrar por año actual
                ).select_for_update().order_by('-id').first()

                # Generar el número correlativo
                if ultimo_folio:
                    try:
                        # Extraer el número correlativo del folio
                        ultimo_numero = int(ultimo_folio.folio.split('-')[3].split('/')[0])
                    except (IndexError, ValueError):
                        ultimo_numero = 0  # Si no se puede extraer, asumir que es 0
                    nuevo_numero = ultimo_numero + 1
                else:
                    nuevo_numero = 1

                # Crear un folio único con prefijo, usuario, correlativo y año
                self.folio = f"{prefijo}-U{self.usuario.id}-{nuevo_numero}/{año_actual}"

        super().save(*args, **kwargs)

    def calcular_totales(self):
        """Calcula los totales de debe y haber basándose en las transacciones."""
        self.debe = sum(trans.debe for trans in self.transacciones.all())
        self.haber = sum(trans.haber for trans in self.transacciones.all())
        self.save()
        

class Transaccion(models.Model):
    registro = models.ForeignKey(Registro, related_name="transacciones", on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    debe = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    haber = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Debe: {self.debe}, Haber: {self.haber}"


#================================================================================================================================================================

def validar_tipo_archivo(archivo):
    valid_extensions = ['pdf', 'jpg', 'png']
    ext = archivo.name.split('.')[-1].lower()
    if ext not in valid_extensions:
        raise ValidationError(f'El archivo {archivo.name} no tiene una extensión permitida. Extensiones válidas: {", ".join(valid_extensions)}.')

class ArchivoAdjunto(models.Model):
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE, related_name="archivos")
    archivo = models.FileField(upload_to="adjuntos/", validators=[validar_tipo_archivo])
    descripcion = models.TextField(blank=True, null=True, default="Sin descripción")
    eliminado = models.BooleanField(default=False)  # Nuevo campo
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)  # Fecha de eliminación opcional

    def eliminar_archivo(self):
        self.eliminado = True
        self.fecha_eliminacion = now()
        self.save()

    def __str__(self):
        return f"Archivo para Registro {self.registro.folio}"


