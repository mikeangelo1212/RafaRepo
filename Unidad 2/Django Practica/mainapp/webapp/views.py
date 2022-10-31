from django.shortcuts import render
from trabajador.models import *

# Create your views here.
def bienvenido(request):
    trabajadores = Trabajador.objects.order_by('id')
    return render(request, 'index.html',{'trabajadores':trabajadores})

def bienvenidoJefes(request):
    jefes = Jefe.objects.order_by('id')
    return render(request, 'indexJefes.html',{'jefes':jefes})

def bienvenidoDepa(request):
    depas = Departamento.objects.order_by('id')
    return render(request, 'indexDepa.html',{'depas':depas})

def bienvenidoDom(request):
    doms = Domicilio.objects.order_by('id')
    return render(request, 'indexDom.html',{'doms':doms})