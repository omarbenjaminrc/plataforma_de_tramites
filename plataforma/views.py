from django.shortcuts import render


# aqui solo van a ir el redireccionamiento al index y 
def index(request):
    return render(request, 'plataforma/index.html')

