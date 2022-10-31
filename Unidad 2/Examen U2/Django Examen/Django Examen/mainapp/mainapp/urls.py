"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from webapp.views import *
from gestorapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bienvenidoAlumnos,name='index'),
    path('tabla_Maestro',bienvenidoMaestros,name='indexMaestros'),
    path('tabla_Directivo',bienvenidoDirectivos,name='indexDirectivos'),
    
    path('detalle_alumno/<int:id>',detalleAlumno),
    path('nuevo_alumno',nuevoAlumno),
    path('editar_alumno/<int:id>',editarAlumno),
    path('eliminar_alumno/<int:id>',eliminarAlumno),
    
    path('detalle_maestro/<int:id>',detalleMaestro),
    path('nuevo_maestro',nuevoMaestro),
    path('editar_maestro/<int:id>',editarMaestro),
    path('eliminar_maestro/<int:id>',eliminarMaestro),
    
    path('detalle_directivo/<int:id>',detalleDirectivo),
    path('nuevo_directivo',nuevoDirectivo),
    path('editar_directivo/<int:id>',editarDirectivo),
    path('eliminar_directivo/<int:id>',eliminarDirectivo),
]
