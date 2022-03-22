from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])  #command for handling requests from Postman
def check_view(request):
    if request.method == 'POST':
        print(request)
        needle = {}
        fact = {}
        material_ids = []
        for value in request.data.items():  #Creating a for loop for request jquery items
            if Product.objects.filter(name=str(value[0])).exists():     #checking existance of requested Product in our Datebase
                product = Product.objects.filter(name=str(value[0])).first()  #selecting the first item of similar products from DB if there are more than one
                qty = value[1]
                if Product_materials.objects.filter(product_id=product.id).exists():    #filtering and checking for existance of IDs of Product_materials relating to Product`s IDs
                    materials = Product_materials.objects.filter(product_id=product.id)
                    for material in materials:  #looping items of Product_materials table
                        materialName = material.material_id.name
                        if materialName not in needle.keys(): #if required Material doesn`t exist in dict called needle, adding it as new material to the dict
                            material_ids.append(material.material_id.id)

                        if product.name not in fact: #additional dictionary for requested products
                            fact[product.name] = []

                        fact[product.name].append({
                            'material_id': material.material_id.id,
                            'material_name': materialName,
                            'material_qty': qty * material.quantity,
                            'product_qty': qty,
                        })

    warehouses = Warehouses.objects.filter(remainder__gte=0).filter(material_id__in=material_ids).values()  #selecting warehouses which contain Product_materials

    response = []

    for key, value in fact.items(): #opening loop fact dictionary`s items for it`s values and keys
        x = {
            'product_name': key,
            'product_qty': 0,
            'product_materials': []
        }
        print(key)
        for val in value:   #looping for values of fact dictionary
            print(val)
            x['product_qty'] = val['product_qty']
            for warehouse in warehouses:
                if val['material_id'] == warehouse['material_id_id'] and val['material_qty'] > 0 and warehouse[
                    'remainder'] > 0:       #setting if condition on equality of FACT dictionary and Warehouse table`s materila IDs and their material quantity existance
                    cnt = min(warehouse['remainder'], val['material_qty'])
                    warehouse['remainder'] -= cnt
                    val['material_qty'] -= cnt

                    x['product_materials'].append({
                        "warehouse_id": warehouse['id'],
                        'material_name': val['material_name'],
                        'qty': cnt,
                        'price': warehouse['price']
                    })  #updating X dictionary with new vaules
            if val['material_qty'] > 0:     #the if condition where there is not enough required materials on specific Product in Warehouses
                x['product_materials'].append({
                    "warehouse_id": None,
                    'material_name': val['material_name'],
                    'qty': val['material_qty'],
                    'price': None
                })
        response.append(x) #final result

    return Response({
        'result': response,
        # 'fact': fact,
        # 'db': warehouses,
    })

