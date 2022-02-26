"""
Cart application urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name="view_cart"),
    path('add/<str:item_id>/', views.AddToCartView.as_view(),
         name="add_to_cart"),
]
