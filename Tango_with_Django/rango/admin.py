from django.contrib import admin
from .models import Category, Page, UserProfile

# admin.site.register(Category)
# admin.site.register(Page)
admin.site.register(UserProfile)

# this is how to edit the interface in the admin webpage 
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)