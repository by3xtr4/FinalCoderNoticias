# Generated by Django 3.2.13 on 2022-07-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0009_consultas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='email_usuario',
            field=models.EmailField(max_length=254),
        ),
    ]