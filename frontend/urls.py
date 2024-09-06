from django.contrib import admin
from django.urls import path

from .views import home, about, portfolio, blog, category;

urlpatterns = [
    path('', home.index, name='index'),
    path('about-us', about.index, name='about'),
    
    path('portfolio', portfolio.index, name='portfolio.index'),
    # portfolio.show
    path('portfolio/<str:slug>', portfolio.show, name='portfolio.show'),
    
    path('blog', blog.index, name='blog.index'),
    path('blog/<str:slug>', blog.show, name='blog.show'),
    
    path('category/<str:slug>', category.show, name='category.show'),
]
