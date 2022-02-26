""" Views of products """
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ View to list all selected items """
    return render(request, "cart/cart.html")


class AddToCartView(View):
    """ Get quanitity from the page and add item to the shopping cart """

    def post(self, request, item_id):
        """ POST method """
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        cart = request.session.get('cart', {})

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             (f'You have {cart[item_id]} of '
                              f'{product.name} in your cart now.'))
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect(redirect_url)
