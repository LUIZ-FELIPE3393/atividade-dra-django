from . import models
from rest_framework import serializers

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cidade
        fields = ['nome', 'ibge']

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoa
        fields = ['nome', 'idade', 'cidade']