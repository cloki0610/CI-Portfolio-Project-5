"""
About application urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.About.as_view(), name="about"),
    path('contact/', views.ContactUs.as_view(), name="contact"),
    path('contact_list/', views.ContactList.as_view(), name="contact_list"),
]
