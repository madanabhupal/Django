from django.urls import path
from myapp.views import *

app_name = 'myapp'

urlpatterns = [
  path('',index, name= 'index'),
  path('<slug:slug>',detail_view, name= 'detail_view'),
]