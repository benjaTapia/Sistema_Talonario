# Generated by Django 5.1.3 on 2024-12-04 12:46

import registros.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivoadjunto',
            name='archivo',
            field=models.FileField(upload_to='adjuntos/', validators=[registros.models.validar_tipo_archivo]),
        ),
    ]
