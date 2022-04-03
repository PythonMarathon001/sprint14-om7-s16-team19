from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='book'),
    path('list/', list_all, name='list_all'),
    path('<int:book_id>/', by_id, name='by_id'),
    path('unordered/', unordered, name='unordered'),
    path('users/', passed),
    path('lookup/', lookup, name='lookup'),
    path('book_list/', book_list, name='book_list'),
]
