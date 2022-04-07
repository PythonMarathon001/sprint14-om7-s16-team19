from django.urls import path
from .views import *

urlpatterns = [
    path('', author_form, name='author_form'),
    path('', AuthorList.as_view(), name='author'),
]
