"""
Product application urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name="products"),
]
