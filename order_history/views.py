""" View of Order History """
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe
from checkout.models import Order
from .forms import OrderReviewForm, CommentForm
from .models import OrderReview

# Create your views here.


class OrderHistoryView(LoginRequiredMixin, View):
    """ Display information of previous order record with comment form """

    def get(self, request, order_number):
        """ GET method """
        order = get_object_or_404(Order, order_number=order_number)
        if (not request.user.userprofile == order.user_profile or not
                request.user.is_superuser):
            messages.warning(request,
                             mark_safe("Access Denied.<br/>"
                                       "Only order owner and admin "
                                       "can read this record."))
        messages.info(request,
                      mark_safe('This is our record of '
                                f'your previous order(Ref. {order_number}). '
                                'Confirmation email should be sent '
                                'on the order date.'))

        return render(request,
                      'order_history/order_history.html',
                      {
                          'order': order,
                      })


class OrderReView(LoginRequiredMixin, View):
    """
    If user do not have its review record, redirect to create page
    Else display the review record with comments
    """

    def get(self, request, slug):
        """ GET method """
        # if no record redirect to create review page
        try:
            order_review = OrderReview.objects.get(slug=slug)
        except OrderReView.ObjectDoesNotExist:
            form = OrderReviewForm()
            messages.warning(request,
                             "You do not write any review yet.\n"
                             "But we're welcome to know something "
                             "about your previous order")
            return render(request,
                          "create_review.html",
                          {
                              'form': form
                          })
        # else return the review detail with comments
        comments = order_review.comments
        comment_form = CommentForm()
        return render(request,
                      'order_history/order_review.html',
                      {
                          'order_review': order_review,
                          'comments': comments,
                          'comment_form': comment_form
                      })


class EditOrderReView(LoginRequiredMixin, View):
    """ Send User a form to edit their existed review """

    def get(self, request, slug):
        """ GET method """
        print(slug)
        return render(request,
                      "order_history/edit_review.html")
# Todo:DeleteOrderReview(post), Comment(post)
