from django.shortcuts import render


def index(request):

    return render(request, 'index.html', {'title': 'Library',
                                         'header': 'Test header', 
                                         'content_title': 'Test content title', 
                                         'content': 'Test content'})
    
def statistics(request):
    return render(request, "statistics.html")

def rules(request):
    return render(request, "rules.html")
