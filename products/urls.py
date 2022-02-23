"""
Product application urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name="products"),
    path('<int:product_pk>/', views.ProductDetailView.as_view(),
         name="product_detail"),
]
