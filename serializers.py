from . import models
from rest_framework import serializers

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estado
        fields = ['nome']

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cidade
        fields = ['nome', 'ibge', 'estado']

'''
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoa
        fields = ['nome', 'idade', 'cidade']

'''