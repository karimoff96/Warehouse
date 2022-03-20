from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    warehouses = Warehouses.objects.all()
    return render(request, 'index.html', {'warehouses': warehouses})

