from django.db import models

class Cidade(models.Model):
    nome = models.TextField(primary_key=True)
    ibge = models.TextField()

class Pessoa(models.Model):
    nome = models.TextField()
    idade = models.IntegerField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)