from django.db import models

class PerifericosNuevos(models.Model):
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)

class PerifericosUsados(models.Model):
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    antiguedad = models.CharField(max_length=50)

class SeBusca(models.Model):
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    antiguedad = models.CharField(max_length=50)