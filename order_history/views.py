""" View of Order History """
from django.shortcuts import (render, get_object_or_404,
                              HttpResponse, redirect, reverse)
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
            return redirect(reverse('home'))
        messages.info(request,
                      mark_safe('This is our record of '
                                f'your previous order(Ref. {order_number}).'
                                '<br/>Confirmation email should be sent '
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

    def get(self, request, order_number, slug):
        """ GET method """
        order = get_object_or_404(Order, order_number=order_number)
        if (not request.user.userprofile == order.user_profile or not
                request.user.is_superuser):
            messages.warning(request,
                             mark_safe("Access Denied.<br/>"
                                       "Only order owner and admin "
                                       "can read this record."))
            return redirect(reverse('home'))
        # if no record redirect to create review page
        try:
            order_review = OrderReview.objects.get(slug=slug)
        except OrderReview.DoesNotExist:
            messages.info(request,
                          mark_safe("You do not write any review yet.<br/>"
                                    "But we're welcome to know something "
                                    "about your previous order"))
            return redirect(reverse('create_view'))
        # else return the review detail with comments
        comments = order_review.comments
        comment_form = CommentForm()
        messages.info(request,
                      mark_safe('This is a review of '
                                f'your previous order(Ref. {order_number}).'
                                '<br/>Feel free to edit or reply your review'
                                'on the order date.'))
        return render(request,
                      'order_history/order_review.html',
                      {
                          'order_review': order_review,
                          'comments': comments,
                          'comment_form': comment_form
                      })

    def post(self, request, order_number, slug):
        """ POST method to submit comment """
        order = get_object_or_404(Order, order_number=order_number)
        order_review = get_object_or_404(OrderReview, slug=slug)
        form = CommentForm(data=request.POST)
        if (not request.user.userprofile == order.user_profile or not
                request.user.is_superuser):
            messages.warning(request,
                             mark_safe("Access Denied.<br/>"
                                       "Only order owner and admin "
                                       "can read this record."))
            return redirect(reverse('home'))
        if form.is_valid():
            comment = form.save(commit=False)
            comment.order_review = order_review
            comment.user = request.user.userprofile
            comment.save()
            messages.success(request,
                             f'Reply on {order.order_number} successfully.')
        else:
            messages.error(request, mark_safe('Invalid Input.<br/>'
                                              'Please check and try again.'))
        return redirect(reverse('order_review'),
                        args=[order.order_number, order_review.slug])


class CreateOrderReView(LoginRequiredMixin, View):
    """ Show a form to create a new review and submit it  """

    def get(self, request, order_number):
        """ GET method """
        order = get_object_or_404(Order, order_number=order_number)
        if (not request.user.userprofile == order.user_profile or not
                request.user.is_superuser):
            messages.warning(request,
                             mark_safe("Access Denied.<br/>"
                                       "Only order owner and admin "
                                       "can do this action."))
            return redirect(reverse('products'))
        form = OrderReviewForm()
        return render(request,
                      "order_history/create_review.html",
                      {
                          'form': form
                      })

    def post(self, request, order_number):
        """ POST method """
        order = get_object_or_404(Order, order_number=order_number)
        if (not request.user.userprofile == order.user_profile or not
                request.user.is_superuser):
            messages.warning(request,
                             mark_safe("Access Denied.<br/>"
                                       "Only order owner and admin "
                                       "can do this action."))
            return redirect(reverse('products'))
        form = OrderReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.order = order
            form.customer = order.user_profile
            form.save()
            messages.success(request,
                             mark_safe('Review Created.<br/>'
                                       'Thank you your support.<br/>'
                                       'If you need any help '
                                       'we will reply soon!'))
        else:
            messages.error(request,
                           mark_safe('Invalid Input.<br/>'
                                     'Please check your input and try again!'))
            return redirect(reverse('order_review'))
        return redirect(reverse('order_review'),
                        args=[order.order_number, form.slug])


class EditOrderReView(LoginRequiredMixin, View):
    """ Send User a form to edit their existed review """

    def get(self, request, order_number, slug):
        """ GET method """
        order = get_object_or_404(Order, order_number=order_number)
        order_review = get_object_or_404(OrderReview, slug=slug)
        if (not request.user.userprofile == order.user_profile or not
                request.user.is_superuser):
            messages.warning(request,
                             mark_safe("Access Denied.<br/>"
                                       "Only order owner and admin "
                                       "can do this action."))
            return redirect(reverse('products'))
        form = OrderReviewForm(instance=order_review)
        return render(request,
                      "order_history/edit_review.html",
                      {
                          'form': form,
                          'order_review': order_review
                      })

    def post(self, request, order_number, slug):
        """ POST method """
        order = get_object_or_404(Order, order_number=order_number)
        order_review = get_object_or_404(OrderReview, slug=slug)
        if (not request.user.userprofile == order.user_profile or not
                request.user.is_superuser):
            messages.warning(request,
                             mark_safe("Access Denied.<br/>"
                                       "Only order owner and admin "
                                       "can do this action."))
            return redirect(reverse('products'))
        form = OrderReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review successfully updated.')
        else:
            messages.error(request,
                           mark_safe('Invalid Input.<br/>'
                                     'Please check your input and try again!'))
        return redirect(reverse('order_review'),
                        args=[order_review.slug])


class DeleteOrderReView(LoginRequiredMixin, View):
    """ Delete order review and return to profile """

    def post(self, request, order_number, slug):
        """ POST method """
        order = get_object_or_404(Order, order_number=order_number)
        order_review = get_object_or_404(OrderReview, slug=slug)
        if (not request.user.userprofile == order.user_profile or not
                request.user.is_superuser):
            messages.warning(request,
                             mark_safe("Access Denied.<br/>"
                                       "Only order owner and admin "
                                       "can do this action."))
            return redirect(reverse('products'))
        try:
            order_review.delete()
            messages.success(request,
                             'Your order review is successfully removed.')
        except Exception as error:
            messages.error(request, f'Action Error: {error}')
            return HttpResponse(status=500)
        return redirect(reverse('profile'))
