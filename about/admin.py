""" Contact model display on admin site """
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Show Contact model in admin site with follow rules """
    list_display = ('name', 'email', 'date',)
    search_fields = ['name', 'message']
    ordering = ('-date',)
