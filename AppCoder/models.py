from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Consultas(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
    detalle = models.CharField(max_length=500)

    def __str__(self):
        return f"Nombre: {self.nombre} - Email {self.email} - detalle_usuario {self.detalle}"

class Cursos(models.Model):
    autor= models.CharField(max_length=30, null=True)
    video = models.CharField(max_length=30, null=True)
    titulo = models.CharField(max_length=100, null=True)
    subtitulo = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    fecha = models.DateField(max_length=20, null=True)

    def __str__(self):
        return f"Autor: {self.autor} - video {self.video}- Titulo {self.titulo} -  Subtitulo {self.subtitulo} - Descripcion {self.descripcion}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"User: {self.user} - imagen {self.imagen} "