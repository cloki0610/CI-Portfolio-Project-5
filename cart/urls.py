"""
Cart application urls
"""
from django.urls import path
from . import views

urlpatterns = [
     path('', views.view_cart, name="view_cart"),
     path('add/<str:item_id>/', views.AddToCartView.as_view(),
          name="add_to_cart"),
     path('delete/<str:item_id>/', views.RemoveItemView.as_view(),
          name="remove_item"),
     path('update/<str:item_id>/', views.UpdateItemView.as_view(),
          name="update_item"),
]
