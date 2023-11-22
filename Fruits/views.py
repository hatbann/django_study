from django.shortcuts import render
from Fruits.models import Fruits

# Create your views here.
def mainPage(request):
    return render(request, 'fruits/index.html')

def createFruitGet(request):
    return render(request, 'fruits/create.html')


def createFruitPost(request):
    fruit = Fruits()
    fruit.name = request.POST.get('fname' , None)
    fruit.descript = request.POST.get('fdescript', None)
    fruit.price = request.POST.get('fprice', None)
    fruit.quantity = request.POST.get('fquantity' , None)

    fruit.save()

    return render(request, 'fruits/createResult.html')

def readFruitGetAll(request):
    fruits = Fruits.objects.all()

    context = {
        'fruits' : fruits
    }
    return render(request, "fruits/list.html", context)

def readFruitGet(request):
    fruits = Fruits.objects.all()

    return render(request, "fruits/read.html")