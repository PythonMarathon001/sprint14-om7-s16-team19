from django.urls import path
from .views import *

urlpatterns = [
    path('list/', BookListAll.as_view(), name='list_all'),
    path('<int:book_id>/', by_id, name='by_id'),
    path('unordered/', unordered, name='unordered'),
    path('lookup/', lookup, name='lookup'),
    path('book_list/', BookListSearch.as_view(), name='book_list'),

]
