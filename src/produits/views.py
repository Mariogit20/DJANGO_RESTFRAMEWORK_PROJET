# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProduitSerializers
from .models import Produits

# Create your views here.
class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produits.objects.all()
    serializer_class = ProduitSerializers