from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.TextField()
    ibge = models.TextField()