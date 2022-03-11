""" Report model display on admin site """
from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """ Show Report model in admin site with follow rules """
    list_filter = ('problem_type', 'checked')
    list_display = ('name', 'problem_type', 'report_on',)
    search_fields = ['name', 'product', 'problem_description']
    ordering = ('-report_on',)
