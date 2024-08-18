from django.shortcuts import render


def index(request):
    context = {
        'title': 'Blog'
    }
    return render(request, 'blog/index.html', context)