from django.shortcuts import render
from book.models import *
from author.models import *

# Create your views here.

def index(request):
    
    return render(request, 'book/index.html', {'title': 'Book...'})


def list_all(request):
    content = Book.get_all()
    return render(request, 'book/list.html', {'title': 'List', 'content_title': 'List of all books' ,'content': content})

def book_list(request):
    
    filter  = {}
    order_by = []
    book_id = ""
    author_id = 0
    name = 'none'
    count = 'none'
    authors = list(Author.objects.all())
    
    if request.method == 'GET':
 
        if 'book_id' in request.GET and not request.GET['book_id'] == "":
            book_id = request.GET['book_id']
            filter['id'] = book_id
            
        if 'author_id' in request.GET and not request.GET['author_id'] == "0":
            author_id = int(request.GET['author_id'])
            #author_obj = Author.objects.get(pk=author_id)
            filter['authors__id'] = author_id
                   
        if 'name' in request.GET and not request.GET['name'] == 'none':
            name = request.GET['name']
            order_by.append('name' if name == 'asc' else '-name')
        
        if 'count' in request.GET and not request.GET['count'] == 'none':
            count = request.GET['count']
            order_by.append('count' if count == 'asc' else '-count')
        
    content = Book.get_all_ordered(order_by, filter)    
    return render(request, 'book/list_part2.html', {'title': 'List', 'content_title': 'List of all books', 'content': content, 'authors':authors, 'filters': {'book_id': book_id, 'author_id': author_id}, 'orders_by': {'name': name, 'count': count}})
