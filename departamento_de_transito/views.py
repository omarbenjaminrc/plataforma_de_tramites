from django.shortcuts import render

# Create your views here.
def departamento_transito(request):
    return render(request, 'departamento_de_transito/departamento_transito.html')

def hora_licencia(request):
    return render(request, 'departamento_de_transito/licencia_de_conducir/descripcion.html')

def login(request):
    return render(request, 'departamento_de_transito/licencia_de_conducir/login.html')

def formulario(request):
    return render(request, 'departamento_de_transito/licencia_de_conducir/formulario.html')

def salida(request):
    return render(request, 'departamento_de_transito/licencia_de_conducir/salida.html')