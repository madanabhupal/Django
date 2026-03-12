from django.shortcuts import render
from myapp.models import Product

# Create your views here.

def index(request):
  products = Product.objects.all()
  print(products)
  return render(request, 'myapp/index.html',{'products':products})