from django.shortcuts import render
from order.models import *

def index(request):
    
    return render(request, 'order/index.html', {'title': 'Order...'})


def order_list(request):
    
    order_by = []
    
    if request.method == 'GET':
        
        data = request.GET
        
        end_at = data['end_at'] if 'end_at' in data else 'asc'
        order_by.append('end_at' if end_at == 'asc' else '-end_at')
        
        plated_end_at = data['plated_end_at'] if 'plated_end_at' in data else 'asc'
        order_by.append('plated_end_at' if plated_end_at == 'asc' else '-plated_end_at')
        
    content = Order.get_all(order_by)    
    return render(request, 'order/list.html', {'title': 'List', 'content_title': 'List of all orders', 'content': content, 'orders_by': {'end_at': end_at, 'plated_end_at': plated_end_at}})
