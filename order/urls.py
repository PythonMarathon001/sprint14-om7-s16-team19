from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='order'),
    path('order_list/', order_list, name='order_list')
]
