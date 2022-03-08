"""
Profiles application urls
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name="profile"),
    path('order_history/<order_number>', include('order_history.urls')),
]
