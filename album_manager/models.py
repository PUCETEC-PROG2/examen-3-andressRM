from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return self.titulo


# Create your models here.
