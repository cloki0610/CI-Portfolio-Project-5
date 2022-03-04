""" Views of checkout """
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from .forms import OrderForm


class CheckoutView(View):
    """ View to display checkout page and post payment request """

    def get(self, request):
        """ GET method """
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, ("You cart still empty, "
                          "please add some item before checkout."))
            return redirect(reverse('products'))

        order_form = OrderForm()
        return render(request,
                      "checkout/checkout.html",
                      {
                          'order_form': order_form
                      })

    def post(self, request):
        """ POST method """
        return render(request,
                      "checkout/checkout.html",
                      {})
