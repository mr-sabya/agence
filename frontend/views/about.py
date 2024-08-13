from django.shortcuts import render


def index(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'about/index.html', context)