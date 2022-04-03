from django.shortcuts import render, redirect
from book.models import Book
from order.models import Order
from author.models import Author
from authentication.models import CustomUser 
from django.db.models.functions import Now
from django.db.models import Q

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

def lookup(request):
    data = request.GET
    if data:
        print(data)
        if data['mode'] == 'name':
            list_of_books = Book.objects.all().filter(name__contains = data['searching'])
        elif data['mode'] == 'description':
            list_of_books = Book.objects.all().filter(description__contains = data['searching'])
        elif data['mode'] == 'author':
            author_ids = Author.objects.all().filter(Q(name__contains = data['searching'])| Q(surname__contains = data['searching'])| Q(patronymic__contains = data['searching'])).values_list('id')
            print(author_ids)
            list_of_books = Book.objects.all().filter(authors__in = author_ids)
    return render(request, 'book/list.html', {'header': f'List of books by {data["mode"]}', 'content': list_of_books})

def passed(request):
    overdu_users_id = Order.objects.all().filter(plated_end_at__lte=Now()).values_list('user_id')
    users_info = CustomUser.objects.all().filter(pk__in = overdu_users_id).values_list('first_name', 'last_name')

