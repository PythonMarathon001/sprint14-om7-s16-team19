from django.urls import path
from .views import *

urlpatterns = [

    path('', OrderList.as_view(), name='order'),
    path('<int:order_id>', order_by_id, name='order_by_id'),
]
