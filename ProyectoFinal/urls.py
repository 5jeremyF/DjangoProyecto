"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mtto.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="inicio"),
# /Materia/ #

    path('materia/',materia, name="materia" ),
    path('agregarmateria/',crearmateria, name="agregarmateria" ),
    path('editarmateria/<int:id>',editarmateria, name="editarmateria" ),
    path('eliminarmateria/<int:id>',eliminarmateria, name="eliminarmateria" ),

# /Profesores/ #

    path('profesores/',profesores, name="profesores" ),
    path('agregarprofesores/',crearprofesores, name="agregarprofesores"),
    path('editarprofesores/<int:id>',editarprofesores, name="editarprofesores"),
    path('eliminarprofesores/<int:id>',eliminarprofesores, name="eliminarprofesores"),

]
