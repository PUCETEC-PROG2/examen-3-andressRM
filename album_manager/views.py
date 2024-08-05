from django.shortcuts import render, redirect
from .forms import ArtistaForm
from .models import Artista

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

# Create your views here.
