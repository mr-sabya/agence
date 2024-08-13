from django.contrib import admin
from django.urls import path

from .views import home, about, portfolio;

urlpatterns = [
    path('', home.index, name='index'),
    path('about-us', about.index, name='about'),
    path('portfolio', portfolio.index, name='portfolio'),
]
