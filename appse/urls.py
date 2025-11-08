from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca_de/', views.acercade, name="acercade"),
    path('mision/', views.visionmision, name="misionvision"),
]