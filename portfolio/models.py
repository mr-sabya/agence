from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# ================================================================================
# ============================== category model start ============================


class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
# ============================== category model end ==============================
# ================================================================================


# ================================================================================
# ========================= Technology member model start =======================
class Technology(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/tech/', blank=True, null=True)
    
    def __str__(self):
        return self.name
# ========================= Technology member model end =========================
# ================================================================================


# ================================================================================
# ============================= portfolio model start ============================
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    description = RichTextUploadingField()
    technologies = models.ManyToManyField(Technology)
    
    def __str__(self) -> str:
        return self.title
# ================================================================================


# ================================================================================
class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self) -> str:
        return self.title
# ================================================================================



# ================================================================================
# ========================= designation member model start =======================
class Degisnation(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
# ========================= designation member model end =========================
# ================================================================================


# ================================================================================
# =========================== team member model start ============================
class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, null=True)
    designation = models.ForeignKey(Degisnation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/team/')
    short_description = models.TextField(null=True, max_length=255)
    details = models.TextField(null=True)
    technologies = models.ManyToManyField(Technology)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
    
# ================================================================================
class Qualification(models.Model):
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    exam = models.CharField(max_length=100)
    year = models.CharField(max_length=15, help_text="2018-2022")
    school = models.CharField(max_length=255)
# ================================================================================


# ================================================================================
class Experience(models.Model):
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    year = models.CharField(max_length=15, help_text="2018-2022")
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
# ================================================================================


# ================================================================================
class Skill(models.Model):
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    progress = models.IntegerField()
# ================================================================================
    
# =========================== team member model end ==============================
# ================================================================================
