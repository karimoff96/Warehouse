from .serializerview import *
from rest_framework import routers
from django.urls import path, include
from .views import *
from .tests import check
router = routers.DefaultRouter()
router.register('products', viewset=ProductApiView)
router.register('materials', viewset=MaterialsApiView)
router.register('product_materials', viewset=Pro_materialsApiView)
router.register('warehouses', viewset=WarehousesApiView)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('api/check', check, name='check'),
    path('api/my_check', check_view, name='my_check')
]
