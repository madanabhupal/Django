from django.shortcuts import render
from myapp.models import Product

# Create your views here.

def index(request):
  product = Product.objects.all()
  return render(request, 'myapp/index.html',{'product':'product'})