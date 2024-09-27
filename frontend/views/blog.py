from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Category, Post


def index(request):
    categories = Category.objects.order_by('id').annotate(posts_count=Count('post'))
    recent_posts = Post.objects.order_by('id')[:4]
    post_count = Post.objects.filter().count()
    
    
    page = request.GET.get('page', 1)
    post_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
        
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



def showCategory(request, slug):
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