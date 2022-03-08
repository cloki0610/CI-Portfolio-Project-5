""" View of Order History """
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from checkout.models import Order

# Create your views here.


class OrderHistoryView(LoginRequiredMixin, View):
    """ Display information of previous order record with comment form """

    def get(self, request, order_number):
        """ GET method """
        order = get_object_or_404(Order, order_number=order_number)

        messages.info(request, (
            f'This is our record of your previous order(Ref. {order_number}). '
            'Confirmation email should be sent on the order date.'
        ))

        return render(request,
                      'order_history/order_history.html',
                      {
                          'order': order,
                      })
