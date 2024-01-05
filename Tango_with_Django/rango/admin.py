from django.contrib import admin
from .models import Category, Page

# admin.site.register(Category)
# admin.site.register(Page)

# this is how to edit the interface in the admin webpage 
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)