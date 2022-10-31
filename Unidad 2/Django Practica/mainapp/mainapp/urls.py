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
from trabajador.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bienvenido,name='index'),
    path('tabla_jefes',bienvenidoJefes,name='indexJefes'),
    path('tabla_depa',bienvenidoDepa,name='indexDepa'),
    path('tabla_dom',bienvenidoDom,name='indexDom'),
    
    path('detalle_trabajador/<int:id>',detalleTrabajador),
    path('nuevo_trabajador',nuevoTrabajador),
    path('editar_trabajador/<int:id>',editarTrabajador),
    path('eliminar_trabajador/<int:id>',eliminarTrabajador),
    
    path('detalle_jefe/<int:id>',detalleJefe),
    path('nuevo_jefe',nuevoJefe),
    path('editar_jefe/<int:id>',editarJefe),
    path('eliminar_jefe/<int:id>',eliminarJefe),
    
    path('detalle_depa/<int:id>',detalleDepa),
    path('nuevo_depa',nuevoDepa),
    path('editar_depa/<int:id>',editarDepa),
    path('eliminar_depa/<int:id>',eliminarDepa),
    
    path('detalle_dom/<int:id>',detalleDom),
    path('nuevo_dom',nuevoDom),
    path('editar_dom/<int:id>',editarDom),
    path('eliminar_dom/<int:id>',eliminarDom),
]
