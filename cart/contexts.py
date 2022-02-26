""" context of the user cart """
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """ return context to view """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quanitity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quanitity * product.price
        product_count += quanitity
        cart_items.append({
            'item_id': item_id,
            'quantity': quanitity,
            'product': product,
        })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    total_cost = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'total_cost': total_cost,
    }

    return context
