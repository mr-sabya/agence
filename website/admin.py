from django.contrib import admin
from .models import Service, Banner, ServiceSection, ServiceFeature, AboutSection, AboutFeature, GoalSection, GoalCounter
# Register your models here.


class bannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Check if there are already any instances of this model
        if Banner.objects.exists():
            # If an instance exists, return False to disable the "Add" button
            return False
        return True
    
    

class ServiceFeatureInline(admin.StackedInline):
    model = ServiceFeature

#service section
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ['name_display']
    inlines = [ServiceFeatureInline]
    
    #
    def has_add_permission(self, request):
        # Check if there are already any instances of this model
        if ServiceSection.objects.exists():
            # If an instance exists, return False to disable the "Add" button
            return False
        return True
    
    
#for about section
class AboutFeatureInline(admin.StackedInline):
    model = AboutFeature
    
    
class aboutSectionAdmin(admin.ModelAdmin):
    inlines = [AboutFeatureInline]
    def has_add_permission(self, request):
        # Check if there are already any instances of this model
        if AboutSection.objects.exists():
            # If an instance exists, return False to disable the "Add" button
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    
#Goal Section
class GoalCounterInline(admin.StackedInline):
    model = GoalCounter
    
class goalSectionAdmin(admin.ModelAdmin):
    inlines = [GoalCounterInline]
    def has_add_permission(self, request):
        # Check if there are already any instances of this model
        if GoalCounter.objects.exists():
            # If an instance exists, return False to disable the "Add" button
            return False
        return True
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    

admin.site.register(Service)
admin.site.register(ServiceSection, ServiceSectionAdmin)
admin.site.register(Banner, bannerAdmin)
admin.site.register(AboutSection, aboutSectionAdmin)
admin.site.register(GoalSection, goalSectionAdmin)