from django.urls import path
from .views import *

urlpatterns = [
    path('', AuthorList.as_view(), name='author'),

]
