from django.urls import path
from .views import *

urlpatterns = [
    path('', author, name='author'),

]
