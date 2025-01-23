from django.shortcuts import render
from .models import Cidade
from .serializers import CidadeSerializer
from rest_framework import generics

# Create your views here.
class CidadeList(generics.ListCreateAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class CidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer