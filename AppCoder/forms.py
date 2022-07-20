from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    #Especificar los campos
    titulo = forms.CharField(max_length=100)
    subtitulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=500)
    autor = forms.CharField(max_length=40)
    video = forms.CharField(max_length=40)
    

class ConsultasFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    email= forms.CharField(max_length=30)
    detalle = forms.CharField(max_length=500)

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
    last_name: forms.CharField()
    first_name: forms.CharField()

    class Meta:
        model = User                                               #agregamos los campos
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        labels = {'username': 'nombre', 'email':'correo','last_name': 'apellido', 'first_name':'nombre'}
        help_texts= {k:"" for k in fields}


class UserEditForm(UserCreationForm): 
    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}