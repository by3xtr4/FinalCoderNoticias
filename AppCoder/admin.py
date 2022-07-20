from django.contrib import admin #traigo esta dependencia, para habilitar el admin
from .models import* #importo models

#registro los modelos en el admin, modelos que ya cree.
#RENOMBRO
admin.site.register(Cursos)
admin.site.register(Consultas)
admin.site.register(Avatar)
