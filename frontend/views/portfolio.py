from django.shortcuts import render


def index(request):
    context = {
        'title': 'Portfolio',
    }
    return render(request, 'portfolio/index.html', context)