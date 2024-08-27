from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

#================================================================================
# banner model start
class Banner(models.Model):
    sub_heading = models.CharField(max_length=255)
    highlight_heading = models.CharField(max_length=15, null=True, blank=True)
    heading = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    # button 1
    button_1_text = models.CharField(max_length=25)
    button_1_link = models.CharField(max_length=255)
    button_2_text = models.CharField(max_length=25)
    button_2_link = models.CharField(max_length=255)

    image = models.ImageField(upload_to='images/banner/')

    def __str__(self):
        return self.highlight_heading + ' '+self.heading

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banner"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Banner, self).delete(*args, **kwargs)
# banner model end
#================================================================================


#================================================================================
# service section model start
class ServiceSection(models.Model):
    sub_heading = models.CharField(max_length=20)
    heading = models.CharField(
        max_length=255, help_text='&lt;span class="title-highlight"&gt;Services&lt;/span&gt; We Can Help You With !')
    text = models.CharField(max_length=255)

    def name_display(self):
        # Example: Wrapping the name in a <strong> tag
        return mark_safe(self.heading)

    def __str__(self):
        return "Service Section"

    class Meta:
        verbose_name = "Service Section"
        verbose_name_plural = "Service Section"


class ServiceFeature(models.Model):
    service_section = models.ForeignKey(
        ServiceSection, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    
# service section model end
#================================================================================


#================================================================================
# service model start
class Service(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title
# service model end
#================================================================================
 

#================================================================================
# about us section model start
class AboutSection(models.Model):
    sub_heading = models.CharField(max_length=15)
    highlight_heading = models.CharField(max_length=15)
    heading = models.CharField(max_length=100)
    text = models.TextField(max_length=255)
    year = models.IntegerField()
    video = models.CharField(
        max_length=100, help_text="Just copy video id from youtube url i.e. <strong>IUN664s7N-c</strong>")
    thumbnail = models.ImageField(upload_to='images/about/')
    image_1 = models.ImageField(upload_to='images/about/')
    image_2 = models.ImageField(upload_to='images/about/')

    def __str__(self):
        return self.highlight_heading + ' '+self.heading

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def delete(self, *args, **kwargs):
        self.thumbnail.delete()
        self.image_1.delete()
        self.image_2.delete()
        super(Banner, self).delete(*args, **kwargs)


class AboutFeature(models.Model):
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
    
# about us section model end
#================================================================================


#================================================================================
# goal section model start
class GoalSection(models.Model):
    sub_heading = models.CharField(max_length=15)
    highlight_heading = models.CharField(max_length=15)
    heading = models.CharField(max_length=100)
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.highlight_heading + ' '+self.heading

    class Meta:
        verbose_name = "Goal Section"
        verbose_name_plural = "Goal Section"
        


class GoalCounter(models.Model):
    goal_section = models.ForeignKey(GoalSection, on_delete=models.CASCADE)
    counter = models.IntegerField(default=0)
    title = models.CharField(max_length=15)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
    
# goal section model end
#================================================================================
