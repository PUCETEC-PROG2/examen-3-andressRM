from django.shortcuts import render, redirect
from .forms import ArtistaForm
from .models import Artista
from django.shortcuts import get_object_or_404
from .forms import AlbumForm
from .models import Album

def home(request):
    return render(request, 'home.html')

def lista_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'lista_artistas.html', {'artistas': artistas})

def crear_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_artistas')  
    else:
        form = ArtistaForm()
    return render(request, 'crear_artista.html', {'form': form})

def actualizar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('lista_artistas')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'actualizar_artista.html', {'form': form})

def eliminar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('lista_artistas')
    return render(request, 'eliminar_artista.html', {'artista': artista})

def lista_albums(request):
    albums = Album.objects.all()
    return render(request, 'lista_albums.html', {'albums': albums})

def crear_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_albums')
    else:
        form = AlbumForm()
    return render(request, 'crear_album.html', {'form': form})

def actualizar_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('lista_albums')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'actualizar_album.html', {'form': form})

def eliminar_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('lista_albums')
    return render(request, 'eliminar_album.html', {'album': album})

# Create your views here.
