from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=100)
    