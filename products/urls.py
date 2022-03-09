"""
Product application urls
"""
from django.urls import path
from . import views

urlpatterns = [
     path('', views.ProductsView.as_view(), name="products"),
     path('<int:product_pk>/', views.ProductDetailView.as_view(),
          name="product_detail"),
     path('add/', views.AddProductView.as_view(), name="add_product"),
     path('edit/<int:product_pk>/', views.EditProductView.as_view(),
          name="edit_product"),
     path('delete_confirm/<int:product_pk>',
          views.DeleteConfirmationView.as_view(), name="delete_confirm"),
     path('delete/<int:product_pk>/', views.DeleteProductView.as_view(),
          name="delete_product"),
]
