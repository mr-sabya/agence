from django.contrib import admin

from .models import Category, Technology, Portfolio, PortfolioImage, Degisnation, TeamMember, Qualification, Experience, Skill
# Register your models here.


#auto generate slug in category model
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}
    list_display = ['title', 'slug']
    


#inline image and technology with portfolio model
class Portfolio_Image(admin.StackedInline):
    model = PortfolioImage
    
    
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}
    list_display = ['title', 'slug']
    list_filter = ["title", "category"]
    inlines = [Portfolio_Image]
    


#inline 
class Team_Member_Qualification(admin.TabularInline):
    model = Qualification
    
class Team_Member_Experience(admin.TabularInline):
    model = Experience
    
class Team_Member_Skill(admin.TabularInline):
    model = Skill
    
    
class TeamMemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}
    inlines = (Team_Member_Qualification, Team_Member_Experience, Team_Member_Skill)
    
    
    
    

#add category to admin panel
admin.site.register(Category, CategoryAdmin)

#add technology to admin panel
admin.site.register(Technology)


# portoflio
admin.site.register(Portfolio, PortfolioAdmin)

#designation and team
admin.site.register(Degisnation)
admin.site.register(TeamMember, TeamMemberAdmin)
