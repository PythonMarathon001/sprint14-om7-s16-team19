from django.shortcuts import render
from order.models import Order
from authentication.models import CustomUser
from django.db.models.functions import Now
from django.db.models import Q
from django.views.generic import ListView


def user_form(request):
    pass  # TODO: add code


class UserList(ListView):
    model = CustomUser
    template_name = "authentication/index.html"
    context_object_name = "users"

    def get(self, request, *args, **kwargs):
        return ListView.get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        context['title'] = 'Список читачів'
        context['content_title'] = 'Адміністрування бібліотеки / Читачі'

        return context

    def get_queryset(self):
        queryset = CustomUser.get_all()

        return queryset


def overdue(request):
    users = CustomUser.objects.filter(Q(order__plated_end_at__lte=Now()) & Q(order__end_at__isnull=True))

    context = {}
    context['title'] = 'Список читачів'
    context['content_title'] = 'Адміністрування бібліотеки / Читачі'
    context['users'] = users

    return render(request, 'authentication/index.html', context)
