from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

# ***********************************************************************
# defino las vistas

urlpatterns = [

    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('nosotros', views.nosotros, name="Nosotros"), #esta era nuestra primer view
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('consultasFormulario', views.consultasFormulario, name="ConsultasFormulario"),
    path('leerCursos', views.leerCursos, name="leerNoticias"),
    path('leerConsultas', views.leerConsultas, name="leerConsultas"),
    path('eliminarConsulta/<id>/', views.eliminarConsulta, name="EliminarConsulta"),
    path('login', views.login_request, name='login'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    path('eliminarCurso/<video>/', views.eliminarCurso, name="EliminarCurso"),
    path('editarCurso/<titulo>/', views.editarCurso, name="EditarCurso"),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('register', views.register, name='register'),
]

