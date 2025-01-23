from . import models
from . import serializers
from rest_framework import generics

# Create your views here.
class CidadeList(generics.ListCreateAPIView):
    queryset = models.Cidade.objects.all()
    serializer_class = serializers.CidadeSerializer

class CidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cidade.objects.all()
    serializer_class = serializers.CidadeSerializer
