from django.db.models import fields
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'mobile', 'new', 'old',
                  'both', 'nothing', 'minimum_q', 'maximum_q', 'pincode')
