from django.shortcuts import render,get_object_or_404,redirect
from gestorapp.forms import *
from gestorapp.models import *

# Create your views here.

def detalleAlumno(request,id):
    alumno = get_object_or_404(Alumnos,pk=id)
    return render(request, 'detalleAlumno.html',{'alumno':alumno})

def nuevoAlumno(request):
    if request.method == "POST":
        formaAlumno = AlumnoForm(request.POST)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('index')
    else:
        formaAlumno = AlumnoForm()
        return render(request,'agregarAlumno.html',{'formaAlumno':formaAlumno})
    
def editarAlumno(request,id):
    alumno = get_object_or_404(Alumnos,pk=id)
    if request.method == "POST":
        formaAlumno = AlumnoForm(request.POST,instance=alumno)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('index')
    else:
        formaAlumno = AlumnoForm(instance=alumno)
        return render(request,'editarAlumno.html',{'formaAlumno':formaAlumno})
    
def eliminarAlumno(request,id):
    alumno = get_object_or_404(Alumnos,pk=id)
    if alumno:
        alumno.delete()
    return redirect('index')

#Maestros

def detalleMaestro(request,id):
    maestro = get_object_or_404(Maestro,pk=id)
    return render(request, 'detalleMaestro.html',{'maestro':maestro})

def nuevoMaestro(request):
    if request.method == "POST":
        formaMaestro = MaestroForm(request.POST)
        if formaMaestro.is_valid():
            formaMaestro.save()
            return redirect('index')
    else:
        formaMaestro = MaestroForm()
        return render(request,'agregarMaestro.html',{'formaMaestro':formaMaestro})
    
def editarMaestro(request,id):
    maestro = get_object_or_404(Maestro,pk=id)
    if request.method == "POST":
        formaMaestro = MaestroForm(request.POST,instance=maestro)
        if formaMaestro.is_valid():
            formaMaestro.save()
            return redirect('index')
    else:
        formaMaestro = MaestroForm(instance=maestro)
        return render(request,'editarMaestro.html',{'formaMaestro':formaMaestro})
    
def eliminarMaestro(request,id):
    maestro = get_object_or_404(Maestro,pk=id)
    if maestro:
        maestro.delete()
    return redirect('index')

#Directivo

def detalleDirectivo(request,id):
    directivo = get_object_or_404(Directivos,pk=id)
    return render(request, 'detalleDirectivo.html',{'directivo':directivo})

def nuevoDirectivo(request):
    if request.method == "POST":
        formaDirectivo = DirectivoForm(request.POST)
        if formaDirectivo.is_valid():
            formaDirectivo.save()
            return redirect('index')
    else:
        formaDirectivo = DirectivoForm()
        return render(request,'agregarDirectivo.html',{'formaDirectivo':formaDirectivo})
    
def editarDirectivo(request,id):
    directivo = get_object_or_404(Directivos,pk=id)
    if request.method == "POST":
        formaDirectivo = DirectivoForm(request.POST,instance=directivo)
        if formaDirectivo.is_valid():
            formaDirectivo.save()
            return redirect('index')
    else:
        formaDirectivo = DirectivoForm(instance=directivo)
        return render(request,'editarDirectivo.html',{'formaDirectivo':formaDirectivo})
    
def eliminarDirectivo(request,id):
    directivo = get_object_or_404(Directivos,pk=id)
    if directivo:
        directivo.delete()
    return redirect('index')