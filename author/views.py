from django.shortcuts import render
from django.views.generic import ListView
from order.models import Author


def author_form(request):
    pass  # TODO: add code


class AuthorList(ListView):
    model = Author
    template_name = "author/index.html"
    context_object_name = "authors"

    def get_context_data(self, **kwargs):
        context = super(AuthorList, self).get_context_data(**kwargs)
        context['title'] = 'Список авторів'
        context['content_title'] = 'Адміністрування бібліотеки / Автори книг'

        return context

    def get_queryset(self):
        queryset = Author.get_all()

        return queryset
