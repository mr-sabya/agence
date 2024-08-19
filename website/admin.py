from django.contrib import admin
from .models import Service, Banner, ServiceSection, ServiceFeature
# Register your models here.


class bannerAdmin(admin.ModelAdmin):
    list_display = ['name_display']
    
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

admin.site.register(Service)
admin.site.register(ServiceSection, ServiceSectionAdmin)
admin.site.register(Banner, bannerAdmin)