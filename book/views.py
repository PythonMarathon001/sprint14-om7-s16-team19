from django.shortcuts import render
from book.models import *

# Create your views here.

def index(request):
    
    return render(request, 'book/index.html', {'title': 'Book...'})


def list_all(request):
    content = Book.get_all()
    return render(request, 'book/list.html', {'title': 'List', 'content_title': 'List of all books' ,'content': content})
