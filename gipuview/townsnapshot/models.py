from django.db import models

# Create your models here.

class Municipio(models.Model):
	name = models.CharField(max_length = 30)

class Tipo(models.Model):
	name = models.CharField(max_length = 30)

class Stats(models.Model):
	municipio = models.ForeignKey(Municipio)
	tipo = models.ForeignKey(Tipo)
	metros = models.IntegerField(default=0)
	contador = models.IntegerField(default=0)
