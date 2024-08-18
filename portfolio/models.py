from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.title
    
    
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    description = models.TextField()


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    
    
class PortfolioTechnology(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)