from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Create your models here.
