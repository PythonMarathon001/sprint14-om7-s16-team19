from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='book'),
    path('list/', list_all, name='list_all'),
    path('<int:book_id>/', by_id, name='by_id'),
    path('unordered/', unordered, name='unordered'),
    path('lookup/', lookup, name='lookup')

]
