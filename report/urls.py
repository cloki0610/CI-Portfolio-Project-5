"""
Report application urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_pk>/', views.ReportView.as_view(), name="report"),
    path('list/', views.ReportListView.as_view(), name="report_list"),
    path('list/<int:report_id>/checked/', views.ReportChecked.as_view(),
         name="report_checked"),
]
