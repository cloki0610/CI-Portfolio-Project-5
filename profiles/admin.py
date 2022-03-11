""" Profile model display on admin site """
from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """ Show model in admin table with follow rules"""
    list_display = ('user',)
    search_fields = ['user', 'default_town_or_city', 'default_country']
