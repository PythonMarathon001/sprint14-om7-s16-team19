from django.urls import path
from .views import *

urlpatterns = [
    path('', authentication, name='authentication'), # http://127.0.0.1:8000/authentication/

]
