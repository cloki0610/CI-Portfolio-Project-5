""" Products model display on admin site """
from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Show Category model in admin site with follow rules """
    list_display = ('name', 'friendly_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Show Product model in admin site with follow rules """
    list_filter = ('category',)
    list_display = ('name', 'category', 'description', 'price')
    search_fields = ['name', 'description']
    ordering = ('sku',)
