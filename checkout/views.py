""" Views of checkout """
import json
import stripe
from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.views import View
from django.contrib import messages
from django.conf import settings
from cart.contexts import cart_contents
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem


class CheckoutView(View):
    """ View to display checkout page and post payment request """

    def get(self, request):
        """ GET method """
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, ("You cart still empty, "
                          "please add some item before checkout."))
            return redirect(reverse('products'))
        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Please check your environment setting and try again.')

        current_cart = cart_contents(request)
        total = current_cart['total_cost']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        order_form = OrderForm()
        return render(request,
                      "checkout/checkout.html",
                      {
                          'order_form': order_form,
                          'stripe_public_key': stripe_public_key,
                          'client_secret': intent.client_secret
                      })

    def post(self, request):
        """ POST method """
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart"
                        " wasn't found in our database. "
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'Form input error. \
                Please check your information and try again.')
            return redirect(reverse('view_cart'))


class CheckoutSuccessView(View):
    """ Redirect to a page with order summary if payment is success """

    def get(self, request, order_number):
        """ GET method """
        save_info = request.session.get('save_info')
        order = get_object_or_404(Order, order_number=order_number)

        messages.success(request, f'Order(Ref:{order_number}) successfully processed! \
            A confirmation email will be sent to {order.email}.')

        if 'cart' in request.session:
            del request.session['cart']

        return render(request,
                      'checkout/checkout_success.html',
                      {
                        'order': order,
                      })


@require_POST
def cache_checkout_data(request):
    """ let user determine save the payment info or not """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as error_msg:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=error_msg, status=400)
