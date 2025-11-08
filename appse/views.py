from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Bienvenido al Sistema Escolar")
    return render(request, "appse/index.html")


def acercade(request):
    return render(request, "appse/acercade.html")


def visionmision(request):
    return render(request, "appse/misionvision.html")