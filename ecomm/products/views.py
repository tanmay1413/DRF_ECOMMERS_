from django.shortcuts import render
from .models import products
from .serializers import ProductsSerializer
from rest_framework import viewsets

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class = ProductsSerializer
