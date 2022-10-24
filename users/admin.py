from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    list_display_links = ['id', 'first_name', 'last_name']
