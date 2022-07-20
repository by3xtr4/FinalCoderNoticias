from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Consultas, Cursos, Avatar
from AppCoder.forms import CursoFormulario, ConsultasFormulario, UserRegisterForm, UserEditForm
from datetime import datetime

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#estas son mis url, diferentes vistas.
def inicio(request): #vista inicio
      return render(request, "AppCoder/inicio.html")

def nosotros(request):#vista usuarios
      return render(request, "AppCoder/nosotros.html")

def leerUsuarios(request):
      profesores = Usuarios.objects.all() #trae todos los profesores
      contexto= {"usuarios":profesores} 
      return render(request, "AppCoder/leerUsuarios.html",contexto)

# cursos, clases
def leerCursos(request):
      cursos = Cursos.objects.all() #trae todos los profesores
      contexto= {"cursos":cursos} 
      return render(request, "AppCoder/leerCursos.html",contexto)

def eliminarCurso(request, nombre):
      curso = Cursos.objects.get(nombre=nombre)
      curso.delete()
      cursos = Cursos.objects.all() #trae todos los profesores
      contexto= {"cursos":cursos} 
      return render(request, "AppCoder/leerCursos.html",contexto)


@login_required
def cursoFormulario(request):#vista usuarios, la edito para que guarde
      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django
                  print(miFormulario)

                  informacion = miFormulario.cleaned_data
                  defino_curso = Cursos (nombre=informacion['nombre'], camada=informacion['camada']) 
                  defino_curso.save()
                  return render(request, "AppCoder/curso_registrado.html", {"mensaje":"Noticia creada con éxito"}) #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/cursoformulario.html", {"miFormulario":miFormulario})


def editarCurso(request, curso_name):

      #Recibe el nombre del profesor que vamos a modificar
      curso = Cursos.objects.get(nombre=curso_name)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  curso.nombre = informacion['nombre']
                  curso.camada = informacion['camada']
                  # curso.fecha = datetime()

                  curso.save() #guardo

                  return render(request, "AppCoder/curso_editado.html", {"mensaje":"Curso actualizado con éxito"}) #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= CursoFormulario(initial={'nombre': curso.nombre, 'camada':curso.camada}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarCurso.html", {"miFormulario":miFormulario, "curso_name":curso_name})


# ***********************************************************************


def leerConsultas(request):
      consultas = Consultas.objects.all() #trae todos los profesores
      contexto= {"consultas":consultas} 
      return render(request, "AppCoder/leerConsultas.html",contexto)

def eliminarConsulta(request, id):
      consulta = Consultas.objects.get(id=id)
      consulta.delete()
      consultas = Consultas.objects.all() 
      contexto= {"consultas":consultas} 
      return render(request, "AppCoder/leerConsultas.html",contexto)





#usuarios,
def productosFormulario(request):#vista usuarios, la edito para que guarde
      if request.method == 'POST':

            miFormulario = ProductosFormulario(request.POST) #aquí mellega toda la información del html - sale de models

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django
                  print(miFormulario)

                  informacion = miFormulario.cleaned_data
                  guardo_producto = Productos (nombre=informacion['nombre'], email=informacion['email'], consulta=informacion['consulta']) 
                  guardo_producto.save()
                  return render(request, "AppCoder/producto_registrado.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProductosFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/productosformulario.html", {"miFormulario":miFormulario})

@login_required
def consultasFormulario(request):#vista usuarios, la edito para que guarde
      if request.method == 'POST':

            miFormulario = ConsultasFormulario(request.POST) #aquí mellega toda la información del html - sale de models

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django
                  print(miFormulario)

                  informacion = miFormulario.cleaned_data
                  guardo_consulta = Consultas (nombre=informacion['nombre'], email=informacion['email'], detalle=informacion['detalle']) 
                  guardo_consulta.save()
                  return render(request, "AppCoder/contacto_enviado.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ConsultasFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/consultasFormulario.html", {"miFormulario":miFormulario})




def productos(request):#vista productos
      return render(request, "AppCoder/productos.html")

def newsletter(request):#vista newsletter
      return render(request, "AppCoder/newsletter.html")



#inicio busqueda cursos inicialmente,
def buscar(request):

      if  request.GET["camada"]: #if request.method == 'Get':

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            print(camada)
            cursos = Cursos.objects.filter(camada__icontains=camada)
            print(cursos)
            return render(request, "AppCoder/resultadoCursos.html", {"cursos":cursos, "camada":camada})
      else: 

	      respuesta = "No enviaste datos"
      return render(request,"AppCoder/cursos.html", {"respuesta":respuesta})

#inicio busqueda cursos inicialmente,
# def buscarUsuario(request):

#       if  request.GET["nombre"]: 
#             nombre = request.GET['nombre'] 
#             print(nombre)
#             registros = Usuarios.objects.filter(nombre__icontains=nombre)
#             print(registros)
#             return render(request, "AppCoder/resultadoUsuarios.html", {"usuarios":registros, "nombre":nombre})
#       else: 

# 	      respuesta = "No enviaste datos"
#       return render(request,"AppCoder/usuarios.html", {"respuesta":respuesta})


def buscarUsuario(request):

      if  request.GET["nombre"]: #if request.method == 'Get':

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            nombre = request.GET['nombre'] 
            print(nombre)
            busuarios = Usuarios.objects.filter(nombre__icontains=nombre)
            print(busuarios)
            return render(request, "AppCoder/resultadoUsuarios.html", {"busuarios":busuarios, "nombre":nombre})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return render(request,"AppCoder/usuarios.html", {"respuesta":respuesta})


def buscarProducto(request):

      if  request.GET["nombre"]: #if request.method == 'Get':
            producto = request.GET['nombre'] 
            print(producto)
            bproductos = Productos.objects.filter(nombre__icontains=producto)
            print(bproductos)
            return render(request, "AppCoder/resultadoProductos.html", {"bproductos":bproductos, "nombre":producto})
      else: 
	      respuesta = "No enviaste datos"

      return render(request,"AppCoder/productos.html", {"respuesta":respuesta})

#iniciamos el login
def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  if user is not None:
                        login(request, user)

                        return render (request, "AppCoder/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        return render (request, "AppCoder/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
      print(3)
      return render(request, "AppCoder/login.html", {'form': form})





def register(request):
      if request.method == "POST":
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "AppCoder/usuario_registrado.html", {"mensaje": "Te has registrado con éxito<br><br>"})

      else: 
            form = UserRegisterForm()

      return render(request, "AppCoder/registro.html", {"form": form})




@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "AppCoder/inicio.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


