from django.contrib import admin
from .models import BlogModel, CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']

