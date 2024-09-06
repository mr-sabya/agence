from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Tag, Post
# Register your models here.


# =======================================================================================
# auto generate slug in category model
class CategoryAdmin(admin.ModelAdmin):

    def action(self, obj):
        action_btn = format_html(
            '<a class="btn btn-primary btn-sm mr-2" href="/admin/blog/category/{}/change/"><i class="fas fa-pencil-alt"></i></a>', obj.id)
        action_btn += format_html(
            '<a class="btn btn-danger btn-sm" href="/admin/blog/category/{}/delete/"><i class="fas fa-trash"></i></a></a>', obj.id)
        return action_btn

    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'slug', 'action']


admin.site.register(Category, CategoryAdmin)
# =======================================================================================


# =======================================================================================
# tag model start
class TagAdmin(admin.ModelAdmin):

    def action(self, obj):
        action_btn = format_html(
            '<a class="btn btn-primary btn-sm mr-2" href="/admin/blog/tag/{}/change/"><i class="fas fa-pencil-alt"></i></a>', obj.id)
        action_btn += format_html(
            '<a class="btn btn-danger btn-sm" href="/admin/blog/tag/{}/delete/"><i class="fas fa-trash"></i></a></a>', obj.id)
        return action_btn

    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'slug', 'action']
    
#tag
admin.site.register(Tag, TagAdmin)
# =======================================================================================


# =======================================================================================
# post model start
class PostAdmin(admin.ModelAdmin):

    def action(self, obj):
        action_btn = format_html(
            '<a class="btn btn-primary btn-sm mr-2" href="/admin/blog/post/{}/change/"><i class="fas fa-pencil-alt"></i></a>', obj.id)
        action_btn += format_html(
            '<a class="btn btn-danger btn-sm" href="/admin/blog/post/{}/delete/"><i class="fas fa-trash"></i></a></a>', obj.id)
        return action_btn

    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'slug', 'action']
    search_fields = ['title', 'category']
    save_as = True


#post
admin.site.register(Post, PostAdmin)
# =======================================================================================
