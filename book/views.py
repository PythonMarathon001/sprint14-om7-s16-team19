from django.shortcuts import render, redirect
from book.models import *
from order.models import *

# Create your views here.

def index(request):
    
    return render(request, 'book/index.html', {'title': 'Book...'})


def list_all(request):
    content = Book.get_all()
    return render(request, 'book/list.html', {'title': 'List', 'content_title': 'List of all books' ,'content': content})

def by_id(request, book_id):

    book_by_id = Book.get_by_id(book_id)
    if book_by_id:
        return render(request, 'book/index.html', {'title': 'book', 'content_title': 'Here is book', 'content': book_by_id})
    else:
        return redirect('book')

def unordered(request):
    ordered_books = Order.objects.all()
    result = Book.objects.exclude(id=1)
    return render(request, 'book/index.html', {'title': 'Unordered', 'content_title':'List of all unordered books', 'content': ['test boo 1', 'test book 2']})
