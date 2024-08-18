from django.contrib import admin
from django.urls import path

from .views import home, about, portfolio, blog;

urlpatterns = [
    path('', home.index, name='index'),
    path('about-us', about.index, name='about'),
    
    path('portfolio', portfolio.index, name='portfolio.index'),
    # portfolio.show
    
    path('blog', blog.index, name='blog.index'),
]
