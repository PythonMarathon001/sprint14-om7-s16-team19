from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view(), name='user'),
    path('overdue/', overdue, name='overdue')

]
