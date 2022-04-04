from django.shortcuts import render
from django.views.generic import ListView
from order.models import Order

class OrderList(ListView):
    
    model = Order
    template_name = "order/list.html"
    context_object_name = "orders"
  
    def get(self, request, *args, **kwargs):
         
        self.order_by = []
        data = request.GET
        
        self.end_at = data['end_at'] if 'end_at' in data else 'asc'
        self.order_by.append('end_at' if self.end_at == 'asc' else '-end_at')
        
        self.plated_end_at = data['plated_end_at'] if 'plated_end_at' in data else 'asc'
        self.order_by.append('plated_end_at' if self.plated_end_at == 'asc' else '-plated_end_at')
              
        return ListView.get(self, request, *args, **kwargs)  
    

    
    def get_context_data(self, **kwargs):
      
        context = super(OrderList, self).get_context_data(**kwargs)
        context['title'] = 'Список замовлень'
        context['content_title'] = 'Адміністрування бібліотеки / Замовлення'
        context['orders_by'] = {'end_at': self.end_at, 'plated_end_at': self.plated_end_at}
       
        return context
   
    def get_queryset(self):
        
        queryset = Order.get_all(self.order_by)

        return queryset     
    
 


def index(request):
    
    return render(request, 'order/index.html', {'title': 'Order...'})


# def order_list(request):
    
#     order_by = []
    
#     if request.method == 'GET':
        
#         data = request.GET
        
#         end_at = data['end_at'] if 'end_at' in data else 'asc'
#         order_by.append('end_at' if end_at == 'asc' else '-end_at')
        
#         plated_end_at = data['plated_end_at'] if 'plated_end_at' in data else 'asc'
#         order_by.append('plated_end_at' if plated_end_at == 'asc' else '-plated_end_at')
        
#     content = Order.get_all(order_by)    
#     return render(request, 'order/list.html', {'title': 'List', 'content_title': 'List of all orders', 'content': content, 'orders_by': {'end_at': end_at, 'plated_end_at': plated_end_at}})
