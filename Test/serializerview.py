from .serializers import *
from .models import *
from rest_framework import viewsets


class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MaterialsApiView(viewsets.ModelViewSet):
    queryset = Materials.objects.all()
    serializer_class = MaterialSerializer


class Pro_materialsApiView(viewsets.ModelViewSet):
    queryset = Product_materials.objects.all()
    serializer_class = Pro_materialSerializer

class WarehousesApiView(viewsets.ModelViewSet):
    queryset = Warehouses.objects.all()
    serializer_class = WarehouseSerializer


