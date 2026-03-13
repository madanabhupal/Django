from django.shortcuts import render
from myapp.models import Product
from django.http import JsonResponse

# Create your views here.

def index(request):
  products = Product.objects.all()
  print(products)
  return render(request, 'myapp/index.html',{'products':products})

def detail_view(request,slug):
  product = Product.objects.get(slug=slug)

  return render(request,'myapp/detail.html',{'product':product})


