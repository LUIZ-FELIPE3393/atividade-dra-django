from . import models
from rest_framework import serializers

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cidade
        fields = ['nome', 'ibge']
