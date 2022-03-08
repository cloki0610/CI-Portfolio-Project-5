"""
order_history application urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderHistoryView.as_view(), name="order_history"),
]
