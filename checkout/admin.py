""" Order, OrderLineItem model display on admin site """
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ Show OrderLine Item in Order model page as inline attribute """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Show Order model in admin site with follow rules """
    inlines = (OrderLineItemAdminInline, )
    readonly_fields = ('order_number', 'user_profile', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid')
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid')
    list_display = ('order_number', 'date', 'full_name',
                    'delivery_cost', 'order_total', 'grand_total')
    ordering = ('-date',)
