""" Products model display on admin site """
from django.contrib import admin
from .models import Product, Category


admin.site.register(Category)
admin.site.register(Product)
