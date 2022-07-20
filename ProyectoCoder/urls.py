from django.contrib import admin
from django.urls import path, include
from AppCoder.views import *
from django.contrib.auth.views import LogoutView
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#defino rutas
urlpatterns = [
    path('AppCoder/admin/', admin.site.urls),

    path('AppCoder/', include('AppCoder.urls')),
 
]

#traigo configuración de avatar
urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)