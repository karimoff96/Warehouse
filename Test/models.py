from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, null=True)
    code = models.CharField(max_length=128, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Materials(models.Model):
    name = models.CharField(max_length=128, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product_materials(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Materials, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0, null=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_id.name


class Warehouses(models.Model):
    material_id = models.ForeignKey(Materials, on_delete=models.CASCADE)
    remainder = models.PositiveIntegerField(default=0, null=True)
    price = models.PositiveIntegerField(default=0, null=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
