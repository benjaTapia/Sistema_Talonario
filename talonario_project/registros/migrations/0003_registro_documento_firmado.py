# Generated by Django 5.1.3 on 2024-12-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_alter_archivoadjunto_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='documento_firmado',
            field=models.FileField(blank=True, null=True, upload_to='documentos_firmados/', verbose_name='Documento Firmado'),
        ),
    ]
