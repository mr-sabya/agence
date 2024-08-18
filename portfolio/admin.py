from django.contrib import admin

from .models import Category, Portfolio, PortfolioImage, PortfolioTechnology
# Register your models here.


#auto generate slug in category model
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}
    list_display = ['title', 'slug']
    


#inline image and technology with portfolio model
class Portfolio_Image(admin.TabularInline):
    model = PortfolioImage
    
class Portfolio_Technology(admin.TabularInline):
    model = PortfolioTechnology
    
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}
    inlines = (Portfolio_Image, Portfolio_Technology)
    
    

#add category to admin panel
admin.site.register(Category, CategoryAdmin)


# portoflio
admin.site.register(Portfolio, PortfolioAdmin)
