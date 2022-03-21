from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'image', 'description', 'created', 'updated']


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'description', 'created', 'updated']


@admin.register(Product_materials)
class Product_materialsAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'material_id', 'quantity', 'image', 'description', 'created', 'updated']


@admin.register(Warehouses)
class WarehousesAdmin(admin.ModelAdmin):
    list_display = ['id', 'material_id', 'remainder', 'price', 'image', 'description', 'created', 'updated',
                    'available']
