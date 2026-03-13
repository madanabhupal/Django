from django.urls import path
from .views import *
 
app_name = 'cart'

urlpatterns=[
  path('add_cart/', add_cart, name='add_cart'),
]