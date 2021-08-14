from django.shortcuts import render, HttpResponse
#importamos Servicio de la app servicios en el archivo models


# Create your views here.

def home(request):

    return render(request, "ProyectoWebApp/home.html")



