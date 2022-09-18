from django.shortcuts import render,redirect
from mtto.forms import *

# Create your views here.

def inicio(request):
    return render(request,"index.html")

# Vistas de Materias
def materia (request):
    materia_form = MateriaForm()
    materia = Materia.objects.all()
    return render(request, "pages/materia.html", {'deparForm':materia_form, 'depar':materia, 'accion': 'Añadir Materias'})


def crearmateria (request):
    if request.method == "POST":
        depar_form = MateriaForm(request.POST)
        if depar_form.is_valid():
            depar_form.save()
            return redirect('materia')
    mate_form = MateriaForm()
    materia = Materia.objects.all()
    return render(request, "pages/agregarmateria.html", {'deparForm':mate_form, 'depar':materia, 'accion': 'Crear'})

def editarmateria(request,id):
    error,depar_form=None,None
    try:
        materia = Materia.objects.get(id=id)
        if request.method=="GET":
            depar_form = MateriaForm(instance=materia)
        else:
            depar_form = MateriaForm(request.POST,instance=materia)
            if depar_form.is_valid():
                depar_form.save()
                return redirect('materia')
    except Exception as e:
        error=e
    
    materia = Materia.objects.all()
    return render(request, "pages/editarmateria.html", {'deparForm':depar_form, 'depar':materia , 'accion': 'Actualizar'})


def eliminarmateria(request,id):
    materia = Materia.objects.get(id=id)
    if request.method=='POST':
        materia.delete()
        return redirect('materia')
    return render(request, 'pages/eliminarmateria.html', {'materia':materia})


# Vistas de Profesores
def profesores (request):
    profesores_form = ProfesoresForm()
    profesores = Profesores.objects.all()
    return render(request, "pages/profesores.html", {'empleadoForm':profesores_form, 'empleados':profesores , 'accion': 'Añadir Profesor'})

def crearprofesores(request):
    if request.method == "POST":
        profesores_form = ProfesoresForm(request.POST)
        if profesores_form.is_valid():
            profesores_form.save()
            return redirect('profesores')
    profesores_form = ProfesoresForm()
    profesores = Profesores.objects.all()
    return render(request, "pages/agregarprofesores.html", {'empleadoForm':profesores_form, 'empleados':profesores , 'accion': 'Crear'})

def editarprofesores(request,id):
    error,profesores_form=None,None
    try:
        profesores = Profesores.objects.get(id=id)
        if request.method=="GET":
            profesores_form = ProfesoresForm(instance=profesores)
        else:
            profesores_form = ProfesoresForm(request.POST,instance=profesores)
            if profesores_form.is_valid():
                profesores_form.save()
                return redirect('profesores')
    except Exception as e:
        error=e
    profesores = Profesores.objects.all()
    return render(request, "pages/editarprofesores.html", {'empleadoForm':profesores_form, 'empleados':profesores , 'accion': 'Actualizar'})

def eliminarprofesores(request,id):
    profesores = Profesores.objects.get(id=id)
    if request.method == 'POST':
        profesores.delete()
        return redirect('profesores')

    return render(request, "pages/eliminarprofesores.html", {'empleado':profesores})
