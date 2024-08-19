from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


#banner
class Banner(models.Model):
    sub_heading = models.CharField(max_length=255)
    heading = models.CharField(max_length=255, help_text='&lt;span class="title-highlight"&gt;Digital&lt;/span&gt; Agency You Can Rely Upon !')
    text = models.CharField(max_length=255)
    
    #button 1
    button_1_text = models.CharField(max_length=25)
    button_1_link = models.CharField(max_length=255)
    button_2_text = models.CharField(max_length=25)
    button_2_link = models.CharField(max_length=255)
    
    image = models.ImageField(upload_to='images/banner/')
    
    
    def name_display(self):
        # Example: Wrapping the name in a <strong> tag
        return mark_safe(self.heading)
    
    def __str__(self):
        return "Hero Section Banner"
    
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Banner, self).delete(*args, **kwargs)
        
        

#service section
class ServiceSection(models.Model):
    sub_heading = models.CharField(max_length=20)
    heading = models.CharField(max_length=255, help_text='&lt;span class="title-highlight"&gt;Services&lt;/span&gt; We Can Help You With !')
    text = models.CharField(max_length=255)
    
    def name_display(self):
        # Example: Wrapping the name in a <strong> tag
        return mark_safe(self.heading)
    
    def __str__(self):
        return "Service Section"
    
class ServiceFeature(models.Model):
    service_section = models.ForeignKey(ServiceSection, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)



#service model
class Service(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    