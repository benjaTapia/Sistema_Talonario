from django import forms
from .models import ArchivoAdjunto, Registro, Transaccion

# Lista de bancos en Santiago de Chile
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

class ArchivoAdjuntoForm(forms.ModelForm):
    class Meta:
        model = ArchivoAdjunto
        fields = ['archivo', 'descripcion']


class RegistroForm(forms.ModelForm):
    banco = forms.ChoiceField(
        choices=BANCOS_CHILE,  # Aquí se carga la lista de bancos
        widget=forms.Select(attrs={'class': 'form-select'}),  # Widget para lista desplegable
        label="Banco",
        error_messages={'required': "El banco es obligatorio."}
    )

    class Meta:
        model = Registro
        fields = [
            'nombre_registro', 'concepto', 'monto', 'cheque_numero',
            'banco', 'detalle', 'tipo_registro', 'documento_firmado'
        ]  # Excluye 'folio'
        widgets = {
            'nombre_registro': forms.TextInput(attrs={'class': 'form-control'}),
            'concepto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'cheque_numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'debe': forms.NumberInput(attrs={'class': 'form-control'}),
            'haber': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_registro': forms.Select(attrs={'class': 'form-select'}),
            'documento_firmado': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'documento_firmado': 'Documento Firmado (opcional)',
        }
        error_messages = {
            'nombre_registro': {
                'required': "El nombre del registro es obligatorio.",
                'max_length': "El nombre no debe exceder los 100 caracteres.",
            },
            'concepto': {
                'required': "El concepto es obligatorio.",
            },
            'monto': {
                'required': "El monto es obligatorio.",
                'invalid': "Debes ingresar un monto válido.",
            },
            'cheque_numero': {
                'invalid': "El número de cheque debe ser un valor numérico.",
            },
            'tipo_registro': {
                'required': "Debes seleccionar un tipo de registro.",
                'invalid_choice': "El tipo de registro seleccionado no es válido.",
            },
            'documento_firmado': {
                'invalid': "El archivo debe ser de un tipo permitido (PDF, DOC, etc.).",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Si el registro ya existe, mostrar el folio pero no permitir editarlo
            self.fields['folio'] = forms.CharField(
                initial=self.instance.folio,
                disabled=True,
                widget=forms.TextInput(attrs={'class': 'form-control'}),
                label="Folio"
            )

    def clean(self):
        """Valida los campos de forma adicional."""
        cleaned_data = super().clean()
        monto = cleaned_data.get("monto")
        debe = cleaned_data.get("debe")
        haber = cleaned_data.get("haber")

        if monto and (monto <= 0):
            self.add_error("monto", "El monto debe ser mayor a 0.")

        if debe and haber and debe + haber > monto:
            raise forms.ValidationError(
                "La suma de 'Debe' y 'Haber' no puede exceder el monto total."
            )

        return cleaned_data


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['descripcion', 'debe', 'haber']
