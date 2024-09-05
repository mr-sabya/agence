from django.shortcuts import render
from django.db.models import Count
from blog.models import Category, Post


def show(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.order_by('id').annotate(posts_count=Count('post'))
    posts = Post.objects.filter(category = category).order_by('id')
    recent_posts = Post.objects.order_by('id')[:4]
    post_count = Post.objects.filter().count()
    
    context = {
        'title': category.title,
        'slug': category.slug,
        'categories': categories,
        'posts': posts,
        'recent_posts': recent_posts,
        'post_count' : post_count
    }
    return render(request, 'blog/index.html', context)