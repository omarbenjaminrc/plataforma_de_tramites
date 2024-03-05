"""
URL configuration for proyecto_plataforma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.departamento_transito, name='index_transito'),
    path('hora_licencia', views.hora_licencia, name='descripcion'),
    path('login', views.login, name='login'),
    path('formulario', views.formulario, name='formulario'),
    path('salida', views.salida, name='salida'),

]