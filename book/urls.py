from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='book'),
    path('list/', list_all, name='list_all')

]
