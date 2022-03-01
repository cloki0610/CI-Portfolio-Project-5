""" Views of products """
from django.shortcuts import render, redirect, get_object_or_404, reverse
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
                             (f'{cart[item_id]} of {product.name} '
                              f'currently in your cart.'))
        else:
            cart[item_id] = quantity
            messages.success(request,
                             (f'{cart[item_id]} of {product.name} '
                              f'currently in your cart.'))

        request.session['cart'] = cart
        return redirect(redirect_url)


class UpdateItemView(View):
    """ View to Update target item in shopping cart """

    def post(self, request, item_id):
        """ POST method """
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request,
                             (f'{cart[item_id]} of {product.name}'
                              f' currently in your cart.'))
        else:
            cart.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your cart'))

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))


class RemoveItemView(View):
    """ View to remove certain item in shopping cart """

    def post(self, request, item_id):
        """ POST method """
        try:
            product = get_object_or_404(Product, pk=item_id)
            cart = request.session.get('cart', {})
            cart.pop(item_id)
            request.session['cart'] = cart
            messages.success(request,
                             f'Removed {product.name} from your cart')
            return redirect(reverse('view_cart'))
        except Exception as error:
            messages.error(request, f'Error action: {error}')
            return redirect(reverse('view_cart'))
