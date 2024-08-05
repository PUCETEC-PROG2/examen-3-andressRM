from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_artista, name='crear_artista'),
    path('artistas/', views.lista_artistas, name='lista_artistas'),
    path('artistas/<int:pk>/actualizar/', views.actualizar_artista, name='actualizar_artista'),
    path('artistas/<int:pk>/eliminar/', views.eliminar_artista, name='eliminar_artista'),
    path('albums/', views.lista_albums, name='lista_albums'),
    path('albums/crear/', views.crear_album, name='crear_album'),
    path('albums/<int:pk>/actualizar/', views.actualizar_album, name='actualizar_album'),
    path('albums/<int:pk>/eliminar/', views.eliminar_album, name='eliminar_album'),
]


# Ingresar tus URLs de la app aquí