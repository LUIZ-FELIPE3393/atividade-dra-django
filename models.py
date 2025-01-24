from django.db import models

class Estado(models.Model):
    nome = models.TextField(primary_key=True)

class Cidade(models.Model):
    nome = models.TextField(primary_key=True)
    ibge = models.TextField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
