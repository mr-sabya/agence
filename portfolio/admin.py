from django.contrib import admin

from .models import Category, Technology, Portfolio, PortfolioImage, Degisnation, TeamMember, Qualification, Experience, Skill, Testimonial, Client
# Register your models here.


# =======================================================================================
# auto generate slug in category model
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'slug']


# add category to admin panel
admin.site.register(Category, CategoryAdmin)
# =======================================================================================


# =======================================================================================
# add technology to admin panel
admin.site.register(Technology)
# =======================================================================================


# =======================================================================================
# add client to admin panel
admin.site.register(Client)
# =======================================================================================


# =======================================================================================
# inline image and technology with portfolio model
class Portfolio_Image(admin.StackedInline):
    model = PortfolioImage


class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'slug']
    list_filter = ["title", "category"]
    inlines = [Portfolio_Image]
    save_as = True


# portoflio
admin.site.register(Portfolio, PortfolioAdmin)
# =======================================================================================


# =======================================================================================
# inline
class Team_Member_Qualification(admin.TabularInline):
    model = Qualification


class Team_Member_Experience(admin.TabularInline):
    model = Experience


class Team_Member_Skill(admin.TabularInline):
    model = Skill


class TeamMemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'designation']
    inlines = (Team_Member_Qualification,
               Team_Member_Experience, Team_Member_Skill)


# designation and team
admin.site.register(Degisnation)
admin.site.register(TeamMember, TeamMemberAdmin)
# =======================================================================================


# =======================================================================================
# testimonial model
class testimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'company']
    
# testimonial
admin.site.register(Testimonial, testimonialAdmin)
# =======================================================================================






