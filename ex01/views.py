from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func1(request):
    num1 = request.GET.get('num1', None)
    num2 = request.GET.get('num2', None)
    context = {'result' : int(num1) + int(num2)}
    return render(request, 'test.html', context)

def func2(request):
    return render(request, 'input.html')

def getPost(request):
    num1 = request.POST.get("num1", None)
    num2 = request.POST.get("num2", None)
    print(type(num1))
    return HttpResponse(int(num1) + int(num2))