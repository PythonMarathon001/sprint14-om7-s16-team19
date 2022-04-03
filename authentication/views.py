from django.shortcuts import render
from order.models import Order
from authentication.models import CustomUser
from django.db.models.functions import Now
from django.db.models import Q

# Create your views here.
def users(request):

    if request.GET:
        overdu_users_id = Order.objects.filter(Q(plated_end_at__lte=Now()) & Q(end_at__isnull = True)).values_list('user_id')
        users_info = CustomUser.objects.filter(pk__in = overdu_users_id).values_list('first_name', 'last_name')
    else:
        users_info = CustomUser.get_all().values_list()

    return render(request, 'authentication/index.html', {'title': 'List', 'content_title': 'List of all books' ,'content': users_info})