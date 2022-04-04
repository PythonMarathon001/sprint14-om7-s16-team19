from django.shortcuts import render


def index(request):

    return render(request, 'index.html', {'title': 'Головна', 
                                         'content_title': 'Громадська бібліотека ім. Т.Г. Шевченко.', 
                                         })
    
def statistics(request):
    return render(request, "statistics.html", {'title': 'Статистика', 
                                         'content_title': 'Адміністрування бібліотеки / Правила та нормативні документи', 
                                         })

def rules(request):
    return render(request, "rules.html", {'title': 'Правила', 
                                         'content_title': 'Адміністрування бібліотеки / Статистика та звіти', 
                                         })
