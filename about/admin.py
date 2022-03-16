""" Contact model display on admin site """
from django.contrib import admin
from .models import Contact, NewsLetter


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Show Contact model in admin site with follow rules """
    list_display = ('name', 'email', 'date',)
    readonly_fields = ('name', 'date')
    search_fields = ['name', 'message']
    ordering = ('-date',)

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    """ Show NewsLetter model in admin site with follow rules """
    list_display = ('email',)
    ordering = ('email',)
