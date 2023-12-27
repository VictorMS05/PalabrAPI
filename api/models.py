from django.db import models

# Create your models here.


class CatalogoPalabras(models.Model):
    """Modelo para el catálogo de palabras de la base de datos"""
    id = models.AutoField(primary_key=True)
    palabra = models.CharField(max_length=25, unique=True, null=False)
    caracteres = models.IntegerField(null=False)
    raiz = models.CharField(max_length=25)
    letra_inicial = models.CharField(max_length=1, null=False)

    objects = models.Manager()
