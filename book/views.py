from django.shortcuts import render, redirect
from book.models import Book
from order.models import Order
from author.models import Author
from authentication.models import CustomUser 
from django.db.models import Q
from django.views.generic import ListView

class BookListSearch(ListView):
    
    model = Book
    template_name = "book/list_part2.html"
    context_object_name = "books"
  
    def get(self, request, *args, **kwargs):
         
        self.filter  = {}
        self.order_by = []
        self.book_id = ""
        self.book_name = ""
        self.author_id = 0
        self.user_id = 0
        self.name = 'none'
        self.count = 'none'
        self.authors = list(Author.objects.all())
        self.users = list(CustomUser.objects.all())
        
        data = request.GET
        
        if 'author_id' in data and not data['author_id'] == "0":
            self.author_id = int(data['author_id'])
            self.filter['authors__id'] = self.author_id
            
        if 'user_id' in data and not data['user_id'] == "0":
            user_filter = {}
            self.user_id =  int(data['user_id'])
            if 'book_id' in data and not data['book_id'] == "":
                self.book_id =  int(data['book_id'])
                user_filter['book__pk'] = self.book_id
            if 'book_name' in data and not data['book_name'] == "":
                self.book_name = data['book_name']
                user_filter['book__name__icontains'] = self.book_name              
                           
            self.user_filter['user__pk'] = self.user_id
            user_books_idlist = [order.book_id for order in list(Order.objects.filter(**user_filter))]
            self.filter['id__in'] = user_books_idlist
        else:
            if 'book_id' in data and not data['book_id'] == "":
                self.book_id = data['book_id']
                self.filter['id'] = self.book_id
            if 'book_name' in data and not data['book_name'] == "":
                self.book_name = data['book_name']
                self.filter['name__icontains'] = self.book_name
                   
        if 'name' in data and not data['name'] == 'none':
            self.name = data['name']
            self.order_by.append('name' if self.name == 'asc' else '-name')
        
        if 'count' in data and not data['count'] == 'none':
            self.count = data['count']
            self.order_by.append('count' if self.count == 'asc' else '-count')     
              
        return ListView.get(self, request, *args, **kwargs)  

    def get_context_data(self, **kwargs):
      
        context = super(BookListSearch, self).get_context_data(**kwargs)
        context['title'] = 'Список книг'
        context['content_title'] = 'Адміністрування бібліотеки / Список книг в наявності'
        context['authors'] = self.authors
        context['users'] = self.users
        context['orders_by'] = {'name': self.name, 'count': self.count}
        context['filters'] = {
                                'book_id': self.book_id,
                                'book_name': self.book_name, 
                                'author_id': self.author_id, 
                                'user_id': self.user_id
                                }
   
        return context
   
    def get_queryset(self):
        
        queryset = Book.get_all_ordered(self.order_by, self.filter)

        return queryset  


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
    ordered = Order.objects.values_list('book_id')
    unordered_books = list(Book.objects.exclude(id__in = ordered))
    return render(request, 'book/list.html', {'title': 'Unordered', 'content_title': 'List of unordered books', 'content': unordered_books})

def lookup(request):
    data = request.GET
    if data:
        print(data)
        if data['mode'] == 'name':
            list_of_books = Book.objects.filter(name__contains = data['searching'])
        elif data['mode'] == 'description':
            list_of_books = Book.objects.filter(description__contains = data['searching'])
        elif data['mode'] == 'author':
            # author_ids = Author.objects.filter(Q(name__contains = data['searching'])| Q(surname__contains = data['searching'])| Q(patronymic__contains = data['searching'])).values_list('id')
            list_of_books = Book.objects.filter(Q(authors__name__contains = data['searching'])| Q(authors__surname__contains = data['searching'])| Q(authors__patronymic__contains = data['searching']))
    return render(request, 'book/list.html', {'header': f'List of books by {data["mode"]}', 'content': list_of_books})

# def book_list(request):
    
#     filter  = {}
#     order_by = []
#     book_id = ""
#     book_name = ""
#     author_id = 0
#     user_id = 0
#     name = 'none'
#     count = 'none'
#     authors = list(Author.objects.all())
#     users = list(CustomUser.objects.all())
    
#     if request.method == 'GET':
        
#         data = request.GET
                
#         if 'author_id' in data and not data['author_id'] == "0":
#             author_id = int(data['author_id'])
#             filter['authors__id'] = author_id
            
#         if 'user_id' in data and not data['user_id'] == "0":
#             user_filter = {}
#             user_id =  int(data['user_id'])
#             if 'book_id' in data and not data['book_id'] == "":
#                 book_id =  int(data['book_id'])
#                 user_filter['book__pk'] = book_id
#             if 'book_name' in data and not data['book_name'] == "":
#                 book_name = data['book_name']
#                 user_filter['book__name__icontains'] = book_name              
                           
#             user_filter['user__pk'] = user_id
#             user_books_idlist = [order.book_id for order in list(Order.objects.filter(**user_filter))]
#             filter['id__in'] = user_books_idlist
#         else:
#             if 'book_id' in data and not data['book_id'] == "":
#                 book_id = data['book_id']
#                 filter['id'] = book_id
#             if 'book_name' in data and not data['book_name'] == "":
#                 book_name = data['book_name']
#                 filter['name__icontains'] = book_name
                   
#         if 'name' in data and not data['name'] == 'none':
#             name = data['name']
#             order_by.append('name' if name == 'asc' else '-name')
        
#         if 'count' in data and not data['count'] == 'none':
#             count = data['count']
#             order_by.append('count' if count == 'asc' else '-count')
        
#     content = Book.get_all_ordered(order_by, filter)    
    
#     return render(request, 
#                   'book/list_part2.html', 
#                   {
#                       'title': 'List', 
#                       'content_title': 'List of all books', 
#                       'content': content, 
#                       'authors':authors, 
#                       'users':users, 
#                       'filters': {
#                           'book_id': book_id,
#                           'book_name': book_name, 
#                           'author_id': author_id, 
#                           'user_id': user_id
#                           },
#                       'orders_by': {
#                           'name': name, 
#                           'count': count
#                           }
#                       })
