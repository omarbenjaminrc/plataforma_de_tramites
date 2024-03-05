from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'plataforma/index.html')

def departamento_transito(request):
    return render(request, 'departamento_de_transito/departamento_transito.html')