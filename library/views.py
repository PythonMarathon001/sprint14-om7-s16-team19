from django.shortcuts import render
from django.http import HttpResponse


def index(request):
     return render(request, "index.html") 
 
def statistics(request):
    return render(request, "statistics.html")

def rules(request):
    return render(request, "rules.html")