from django.shortcuts import render
from django.db.models import Count
from blog.models import Category, Post


def index(request):
    categories = Category.objects.order_by('id').annotate(posts_count=Count('post'))
    posts = Post.objects.order_by('id')
    recent_posts = Post.objects.order_by('id')[:4]
    post_count = Post.objects.filter().count()
    
    context = {
        'title': 'Blog',
        'slug': 'all',
        'categories': categories,
        'posts': posts,
        'recent_posts': recent_posts,
        'post_count': post_count,
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