from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# ================================================================================
# category model start ===========================================================


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
# category model end =============================================================
# ================================================================================


# ================================================================================
# tag model start ================================================================
class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
# tag model end ==================================================================
# ================================================================================


# ================================================================================
# post model start ===============================================================
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.TextField(max_length=255)
    description = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='images/blog/')
    image = models.ImageField(upload_to='images/blog/')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
# post model end =================================================================
# ================================================================================
