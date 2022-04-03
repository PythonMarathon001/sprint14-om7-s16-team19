from django.shortcuts import render, redirect
from book.models import Book
from order.models import Order
from author.models import Author
from authentication.models import CustomUser 
from django.db.models.functions import Now

# Create your views here.

def index(request):
    
    return render(request, 'book/index.html', {'title': 'Book...'})


def list_all(request):
    content = Book.get_all()
    return render(request, 'book/book_list.html', {'title': 'List', 'content_title': 'List of all books' ,'content': content})

def by_id(request, book_id):

    book_by_id = Book.get_by_id(book_id)
    if book_by_id:
        return render(request, 'book/index.html', {'title': 'book', 'content_title': 'Here is book', 'content': book_by_id})
    else:
        return redirect('book')

def unordered(request):
    ordered = Order.objects.all().values_list('book_id')
    unordered_books = list(Book.objects.all().exclude(id__in = ordered))
    return render(request, 'book/list.html', {'title': 'Unordered', 'content_title': 'List of unordered books', 'content': unordered_books})

def passed(request):
    overdu_users_id = Order.objects.all().filter(plated_end_at__lte=Now()).values_list('user_id')
    users_info = CustomUser.objects.all().filter(pk__in = overdu_users_id).values_list('first_name', 'last_name')

