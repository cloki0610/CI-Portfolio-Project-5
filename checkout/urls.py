"""
Checkout application urls
"""
from django.urls import path
from .webhooks import webhook
from . import views

urlpatterns = [
    path('', views.CheckoutView.as_view(), name="checkout"),
    path('checkout_success/<order_number>',
         views.CheckoutSuccessView.as_view(), name="checkout_success"),
    path('wh/', webhook, name='webhook'),
    path('cache_checkout_data/',
         views.cache_checkout_data, name='cache_checkout_data'),
]
