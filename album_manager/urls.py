from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_artista, name='crear_artista'),
    path('artistas/', views.lista_artistas, name='lista_artistas'),
    
]


# Ingresar tus URLs de la app aquí