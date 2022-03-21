from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def check_view(request):
    if request.method == 'POST':
        needle = {}
        fact = {}
        material_ids = []

        for value in request.data.items():
            if Product.objects.filter(name=str(value[0])).exists():
                product = Product.objects.filter(name=str(value[0])).first()
                qty = value[1]
                if Product_materials.objects.filter(product_id=product.id).exists():
                    materials = Product_materials.objects.filter(product_id=product.id)
                    for material in materials:
                        materialName = material.material_id.name
                        if materialName not in needle.keys():
                            material_ids.append(material.material_id.id)

                        if product.name not in fact:
                            fact[product.name] = []

                        fact[product.name].append({
                            'material_id': material.material_id.id,
                            'material_name': materialName,
                            'material_qty': qty * material.quantity,
                            'product_qty': qty,
                        })

    warehouses = Warehouses.objects.filter(remainder__gte=0).filter(material_id__in=material_ids).values()

    response = []

    for key, value in fact.items():
        x = {
            'product_name': key,
            'product_qty': 0,
            'product_materials': []
        }
        print(key)
        for val in value:
            print(val)
            x['product_qty'] = val['product_qty']
            for warehouse in warehouses:
                if val['material_id'] == warehouse['material_id_id'] and val['material_qty'] > 0 and warehouse[
                    'remainder'] > 0:
                    cnt = min(warehouse['remainder'], val['material_qty'])
                    warehouse['remainder'] -= cnt
                    val['material_qty'] -= cnt

                    x['product_materials'].append({
                        "warehouse_id": warehouse['id'],
                        'material_name': val['material_name'],
                        'qty': cnt,
                        'price': warehouse['price']
                    })
            if val['material_qty'] > 0:
                x['product_materials'].append({
                    "warehouse_id": None,
                    'material_name': val['material_name'],
                    'qty': val['material_qty'],
                    'price': None
                })
        response.append(x)

    return Response({
        'result': response,
        # 'fact': fact,
        # 'db': warehouses,
    })
