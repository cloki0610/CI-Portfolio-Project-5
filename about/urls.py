"""
About application urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.About.as_view(), name="about"),
    path('contact_us/', views.ContactUs.as_view(), name="contact_us"),
    path('contact_list/', views.ContactList.as_view(), name="contact_list"),
]
