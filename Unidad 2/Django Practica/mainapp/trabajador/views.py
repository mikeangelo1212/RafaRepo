import re
from django.shortcuts import render,get_object_or_404,redirect
from trabajador.forms import *
from trabajador.models import *

# Create your views here.

def detalleTrabajador(request,id):
    trabajador = get_object_or_404(Trabajador,pk=id)
    return render(request, 'detalleTrabajador.html',{'trabajador':trabajador})

def nuevoTrabajador(request):
    if request.method == "POST":
        formaTrabajador = TrabajadorForm(request.POST)
        if formaTrabajador.is_valid():
            formaTrabajador.save()
            return redirect('index')
    else:
        formaTrabajador = TrabajadorForm()
        return render(request,'agregarTrabajador.html',{'formaTrabajador':formaTrabajador})
    
def editarTrabajador(request,id):
    trabajador = get_object_or_404(Trabajador,pk=id)
    if request.method == "POST":
        formaTrabajador = TrabajadorForm(request.POST,instance=trabajador)
        if formaTrabajador.is_valid():
            formaTrabajador.save()
            return redirect('index')
    else:
        formaTrabajador = TrabajadorForm(instance=trabajador)
        return render(request,'editarTrabajador.html',{'formaTrabajador':formaTrabajador})
    
def eliminarTrabajador(request,id):
    trabajador = get_object_or_404(Trabajador,pk=id)
    if trabajador:
        trabajador.delete()
    return redirect('index')

#Jefes

def detalleJefe(request,id):
    jefe = get_object_or_404(Jefe,pk=id)
    return render(request, 'detalleJefe.html',{'jefe':jefe})

def nuevoJefe(request):
    if request.method == "POST":
        formaJefe = JefeForm(request.POST)
        if formaJefe.is_valid():
            formaJefe.save()
            return redirect('indexJefes')
    else:
        formaJefe = JefeForm()
        return render(request,'agregarJefe.html',{'formaJefe':formaJefe})
    
def editarJefe(request,id):
    jefe = get_object_or_404(Jefe,pk=id)
    if request.method == "POST":
        formaJefe = JefeForm(request.POST,instance=jefe)
        if formaJefe.is_valid():
            formaJefe.save()
            return redirect('indexJefes')
    else:
        formaJefe = JefeForm(instance=jefe)
        return render(request,'editarJefe.html',{'formaJefe':formaJefe})
    
def eliminarJefe(request,id):
    jefe = get_object_or_404(Jefe,pk=id)
    if jefe:
        jefe.delete()
    return redirect('indexJefes')

#Depa

def detalleDepa(request,id):
    depa = get_object_or_404(Departamento,pk=id)
    return render(request, 'detalleDepa.html',{'depa':depa})

def nuevoDepa(request):
    if request.method == "POST":
        formaDepa = DepaForm(request.POST)
        if formaDepa.is_valid():
            formaDepa.save()
            return redirect('indexDepa')
    else:
        formaDepa = DepaForm()
        return render(request,'agregarDepa.html',{'formaDepa':formaDepa})
    
def editarDepa(request,id):
    depa = get_object_or_404(Departamento,pk=id)
    if request.method == "POST":
        formaDepa = DepaForm(request.POST,instance=depa)
        if formaDepa.is_valid():
            formaDepa.save()
            return redirect('indexDepa')
    else:
        formaDepa = DepaForm(instance=depa)
        return render(request,'editarDepa.html',{'formaDepa':formaDepa})
    
def eliminarDepa(request,id):
    depa = get_object_or_404(Departamento,pk=id)
    if depa:
        depa.delete()
    return redirect('indexDepa')

#Dom

def detalleDom(request,id):
    dom = get_object_or_404(Domicilio,pk=id)
    return render(request, 'detalleDom.html',{'dom':dom})

def nuevoDom(request):
    if request.method == "POST":
        formaDom = DomForm(request.POST)
        if formaDom.is_valid():
            formaDom.save()
            return redirect('indexDom')
    else:
        formaDom = DomForm()
        return render(request,'agregarDom.html',{'formaDom':formaDom})
    
def editarDom(request,id):
    dom = get_object_or_404(Domicilio,pk=id)
    if request.method == "POST":
        formaDom = DomForm(request.POST,instance=dom)
        if formaDom.is_valid():
            formaDom.save()
            return redirect('indexDom')
    else:
        formaDom = DomForm(instance=dom)
        return render(request,'editarDom.html',{'formaDom':formaDom})
    
def eliminarDom(request,id):
    dom = get_object_or_404(Domicilio,pk=id)
    if dom:
        dom.delete()
    return redirect('indexDom')