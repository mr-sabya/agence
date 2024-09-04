from django.contrib import admin
from .models import Service, Banner, ServiceSection, ServiceFeature, AboutSection, AboutFeature, GoalSection, GoalCounter, TeamSection, PortfolioSection
from .models import TestimonialSection
# Register your models here.


# =======================================================================================
# for banner section
class bannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Check if there are already any instances of this model
        if Banner.objects.exists():
            # If an instance exists, return False to disable the "Add" button
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


# banner
admin.site.register(Banner, bannerAdmin)
# =======================================================================================


# =======================================================================================
# for service section
class ServiceFeatureInline(admin.StackedInline):
    model = ServiceFeature

# service section


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

    def has_delete_permission(self, request, obj=None):
        return False


# service section
admin.site.register(ServiceSection, ServiceSectionAdmin)
admin.site.register(Service)
# =======================================================================================


# =======================================================================================
# for about section
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


# about section
admin.site.register(AboutSection, aboutSectionAdmin)
# =======================================================================================


# =======================================================================================
# for Goal Section
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


# goal section
admin.site.register(GoalSection, goalSectionAdmin)
# =======================================================================================


# =======================================================================================
# for team section
class teamSectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Check if there are already any instances of this model
        if TeamSection.objects.exists():
            # If an instance exists, return False to disable the "Add" button
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


# team section
admin.site.register(TeamSection, teamSectionAdmin)
# =======================================================================================


# =======================================================================================
# for portfolio section
class portfolioSectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Check if there are already any instances of this model
        if PortfolioSection.objects.exists():
            # If an instance exists, return False to disable the "Add" button
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


# portfolio section
admin.site.register(PortfolioSection, portfolioSectionAdmin)
# =======================================================================================


# =======================================================================================
# for testimonial section
class testimonialSectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Check if there are already any instances of this model
        if TestimonialSection.objects.exists():
            # If an instance exists, return False to disable the "Add" button
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


# testimonial section
admin.site.register(TestimonialSection, testimonialSectionAdmin)
# =======================================================================================