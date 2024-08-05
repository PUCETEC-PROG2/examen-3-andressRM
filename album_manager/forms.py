from django import forms
from .models import Artista
from .models import Album

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'pais_origen']

class AlbumForm(forms.ModelForm):
    fecha_lanzamiento = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    )

    class Meta:
        model = Album
        fields = ['titulo', 'artista', 'fecha_lanzamiento']