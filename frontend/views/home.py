from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home/index.html', context)