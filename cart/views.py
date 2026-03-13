from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def add_cart(request):
  if request.method == 'POST':
    product_id = request.POST.get('product_id')
    product_quantity = request.POST.get('product_quantity')
    print('product_id ',product_id)
    print('product_quantity :',product_quantity)
  return JsonResponse({'Message':'Add to cart button clicked'})