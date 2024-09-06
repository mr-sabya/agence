from django.shortcuts import render
from portfolio.models import Portfolio, Category

def index(request):
    projects = Portfolio.objects.order_by('-id')
    
    context = {
        'title': 'Portfolio',
        'projects': projects
    }
    return render(request, 'portfolio/index.html', context)


def show(request, slug):
    project = Portfolio.objects.get(slug=slug)
    categories = Category.objects.order_by('id')
    context = {
        'title': project.title,
        'project': project,
        'categories': categories
    }
    return render(request, 'portfolio/show.html', context)