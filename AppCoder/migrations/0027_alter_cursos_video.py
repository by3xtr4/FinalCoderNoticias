# Generated by Django 3.2.13 on 2022-07-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0026_rename_camada_cursos_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='video',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
