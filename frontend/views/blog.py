from django.shortcuts import render
from django.db.models import Count
from blog.models import Category, Post


def index(request):
    categories = Category.objects.order_by('id').annotate(posts_count=Count('post'))
    posts = Post.objects.order_by('id')
    recent_posts = Post.objects.order_by('id')[:4]
    
    context = {
        'title': 'Blog',
        'categories': categories,
        'posts': posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/index.html', context)


def show(request, slug):
    categories = Category.objects.order_by('id').annotate(posts_count=Count('post'))
    recent_posts = Post.objects.order_by('id')[:4]
    post = Post.objects.get(slug=slug)
    
    context = {
        'title': 'Blog',
        'categories': categories,
        'recent_posts': recent_posts,
        'post': post
    }
    return render(request, 'blog/show.html', context)