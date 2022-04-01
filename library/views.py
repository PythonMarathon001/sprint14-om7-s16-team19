from django.shortcuts import render


def index(request):

    return render(request, 'index.html', {'title': 'Library',
                                         'header': 'Test header', 
                                         'content_title': 'Test content title', 
                                         'content': 'Test content'})