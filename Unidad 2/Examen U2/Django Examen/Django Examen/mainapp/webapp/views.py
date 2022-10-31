from django.shortcuts import render
from gestorapp.models import *

# Create your views here.

def bienvenidoAlumnos(request):
    alumnos = Alumnos.objects.order_by('id')
    return render(request, 'index.html',{'alumnos':alumnos})

def bienvenidoMaestros(request):
    maestros = Maestro.objects.order_by('id')
    return render(request, 'indexMaestros.html',{'maestros':maestros})

def bienvenidoDirectivos(request):
    directivos = Directivos.objects.order_by('id')
    return render(request, 'indexDirectivos.html',{'directivos':directivos})