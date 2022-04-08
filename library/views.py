from django.shortcuts import render


def not_found_404(request):
    return render(request, 'index.html',
                  {'title': '404',
                   'content_title': 'Громадська бібліотека ім. Т.Г. Шевченко.',
                   'content': 'Error 404: Data you are searching not found...',
                   })


def index(request):
    return render(request, 'index.html',
                  {'title': 'Головна',
                   'content_title': 'Громадська бібліотека ім. Т.Г. Шевченко.',
                   })


def statistics(request):
    return render(request, "statistics.html",
                  {'title': 'Статистика',
                   'content_title': 'Адміністрування бібліотеки / Правила та нормативні документи',
                   })


def rules(request):
    return render(request, "rules.html",
                  {'title': 'Правила',
                   'content_title': 'Адміністрування бібліотеки / Статистика та звіти',
                   })


def reconstruction(request):
    return render(request, "reconstruction.html",
                  {'title': 'Розділ на реконструції',
                   'content_title': 'Розділ на реконструції',
                   })
