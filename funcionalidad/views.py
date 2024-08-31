from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Personal, Tipo
from .forms import PersonalForm, TipoForm
from django.contrib import messages


#inicio
def inicial (request):
    return render (request, 'inicio.html')

#Registrar Usuarios
def registrar(request):
    if request.method == 'GET':
       return render (request, 'registrar.html', {
        'from': UserCreationForm
       })
    else:
        if request.POST['password']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST
                    ['password'], email=request.POST['email'], first_name=request.POST['first_name'])
                user.save()
                login(request, user)
                return redirect('registros')
            except IntegrityError:
                return render (request, 'registrar.html', {
                    'from': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
                
        return render (request, 'registrar.html', {
            'from': UserCreationForm })


#Loguearse
def ingresar(request):
    if request.method == 'GET':
       return render(request, 'ingresar.html',{
       'form': AuthenticationForm 
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render (request, 'ingresar.html', {
                'form': AuthenticationForm,
                'error': 'Datos Invalidos, asegurate de ingresarlos correctamente'
            })
        else:   
            login(request, user)
            return redirect('registros')

#sesion iniciada
@login_required(login_url='/ingresar')
def danshboard (request):
    Datos = Personal.objects.filter( 
    usuario = request.user.id)
    return render (request, 'registros.html', {'Personal': Datos})

@login_required(login_url='/ingresar')
def cuenta (request):
    return render (request, 'cuenta.html')
  

#Formulario
@login_required(login_url='/ingresar')
def personal (request):
    form = PersonalForm(request.POST or None)
    tipos = list(Tipo.objects.all())
    print(request.POST)
    if request.POST:
        if form.is_valid():
            form.save() 
            return redirect('registros')   
        else:
            return render (request, 'nuevopersonal.html', {"form":form, "tipos":tipos})         
    else: 
        form = PersonalForm()
        return render (request, 'nuevopersonal.html', {"form":form, "tipos":tipos})
    
def editar (request, id):
  datos = get_object_or_404 (Personal, id=id)
  form = PersonalForm(request.POST or None,instance=datos)
  tipos= list(Tipo.objects.all())
  print(request.POST)
  contenido= {'form': form , "tipos":tipos}
  if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/registros')
        else:
            return render (request, 'editar.html', contenido)
  else:
    form=PersonalForm(instance=datos)
    return render (request, 'editar.html', contenido)
    


def eliminar(request, id):
    dato = get_object_or_404 (Personal, id=id)
    dato.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to='/registros')