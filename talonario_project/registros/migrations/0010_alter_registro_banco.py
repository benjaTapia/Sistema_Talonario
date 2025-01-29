# Generated by Django 5.1.4 on 2024-12-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0009_registro_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='banco',
            field=models.CharField(blank=True, choices=[('Sin Detalles', 'Sin Detalles'), ('Banco de Chile', 'Banco de Chile'), ('BancoEstado', 'BancoEstado'), ('Banco Santander', 'Banco Santander'), ('Banco BCI', 'Banco BCI'), ('Banco Itaú', 'Banco Itaú'), ('Scotiabank Chile', 'Scotiabank Chile'), ('Banco Ripley', 'Banco Ripley'), ('Banco Falabella', 'Banco Falabella'), ('Banco Security', 'Banco Security')], max_length=50, null=True),
        ),
    ]
