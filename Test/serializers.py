from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'code')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ('id', 'name')


class Pro_materialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_materials
        fields = ('id', 'product_id', 'material_id', 'quantity')


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouses
        fields = ('id', 'material_id', 'remainder', 'price')
