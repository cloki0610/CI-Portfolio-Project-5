"""
Report application urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_pk>/', views.ReportView.as_view(), name="report"),
    path('list/', views.ReportListView.as_view(), name="report_list"),
]
