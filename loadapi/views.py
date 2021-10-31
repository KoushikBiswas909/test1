from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serialize import ProductSerializer

# Create your views here.


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
