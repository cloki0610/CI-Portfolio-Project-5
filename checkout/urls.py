"""
Checkout application urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CheckoutView.as_view(), name="checkout"),
]
