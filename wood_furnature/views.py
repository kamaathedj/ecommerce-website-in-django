from django.shortcuts import render
from .models import wood_metal
import secrets
import json
from wood_furnature.mpesa.pay import mpesaTransact


# Create your views here.

def index(request):
    
    wood = wood_metal.objects.order_by('-updated')
    wood_list = []
    for woods in wood:
        furnature = {
            'name': woods.name,
            'description': woods.description,
            'price': woods.price,
            'image': woods.furnature_image,
            'id': woods.id
        }
        wood_list.append(furnature)
       

    context = {'wood_list': wood_list}

    return render(request, 'wood/index.html', context)


def details(request, id):
    wood = wood_metal.objects.get(id=id)
    context = {
        'wood': wood
    }
     
    return render(request, 'wood/detail.html',context)

def amPaying(request,id):
    wood = wood_metal.objects.get(id=id)
    if request.method=='POST':
        k=secrets.token_hex(16)
        m=json.loads(mpesaTransact(wood.price,0727937153,""))
        print(m)
    
    context = {
        'wood': wood
    }

    return render(request,'wood/payments.html',context)


    


