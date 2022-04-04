from django.urls import path
from .views import *

urlpatterns = [
    #path('', order_list, name='order'),
    path('', OrderList.as_view(), name='order'),
    #path('order_list/', order_list, name='order_list')
]
