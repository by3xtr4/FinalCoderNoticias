# Generated by Django 3.2.13 on 2022-07-19 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0017_auto_20220719_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='encabezado',
            new_name='camada',
        ),
        migrations.RenameField(
            model_name='cursos',
            old_name='titulo',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='detalle',
        ),
    ]
