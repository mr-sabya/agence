from django.contrib import admin
from django.urls import path

from .views import home, about;

urlpatterns = [
    path('', home.index, name='index'),
    path('about-us', about.index, name='about'),
]
