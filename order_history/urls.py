"""
order_history application urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderHistoryView.as_view(), name="order_history"),
    path('create/', views.CreateOrderReView.as_view(), name="create_review"),
    path('<slug:slug>/', views.OrderReView.as_view(), name="order_review"),
    path('<slug:slug>/update/', views.UpdateOrderReView.as_view(),
         name="update_review"),
    path('<slug:slug>/delete/', views.DeleteOrderReView.as_view(),
         name="delete_review"),
]
