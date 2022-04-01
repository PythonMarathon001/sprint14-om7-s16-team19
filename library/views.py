from django.shortcuts import render


def index(request):

    return render(request, 'index.html', {'header': 'Test header', 'content_title': 'Test content title', 'content': 'Test content'})