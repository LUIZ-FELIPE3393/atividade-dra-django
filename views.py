from . import models
from . import serializers
from rest_framework import generics

class CidadeList(generics.ListCreateAPIView):
    queryset = models.Cidade.objects.all()
    serializer_class = serializers.CidadeSerializer


class CidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cidade.objects.all()
    serializer_class = serializers.CidadeSerializer


class EstadoList(generics.ListCreateAPIView):
    queryset = models.Estado.objects.all()
    serializer_class = serializers.EstadoSerializer


class EstadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Estado.objects.all()
    serializer_class = serializers.EstadoSerializer

'''
 
class PessoaList(generics.ListCreateAPIView):
    queryset = models.Pessoa.objects.all()
    serializer_class = serializers.EstadoSerializer


class PessoaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pessoa.objects.all()
    serializer_class = serializers.PessoaSerializer

'''