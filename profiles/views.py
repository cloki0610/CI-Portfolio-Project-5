""" View of profiles """
from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe
from checkout.models import Order
from .forms import UserProfileForm


class ProfileView(LoginRequiredMixin, View):
    """ View to display and edit user profile """

    def get(self, request):
        """ GET method """
        profile = request.user.userprofile
        orders = profile.orders.all()
        profile_form = UserProfileForm(instance=request.user.userprofile)
        messages.info(request,
                      mark_safe('If you need to edit your profile.<br/>'
                                'Please know that your Full name and E-mail '
                                'are required.'))
        return render(request,
                      "profiles/profile.html",
                      {
                          'profile_form': profile_form,
                          'orders': orders,
                          'on_profile_page': True
                      })

    def post(self, request):
        """ POST method """
        profile_form = UserProfileForm(request.POST,
                                       instance=request.user.userprofile)
        # form validation and show the result as message
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your Profile Has Updated.')
        else:
            messages.error(request,
                           mark_safe('Updated Invalid.<br/>'
                                     'Please check and try again!'))
        return redirect(reverse('profile'))


class DeleteAccount(LoginRequiredMixin, View):
    """ confirm page for delete account """

    def get(self, request):
        """ get method """
        # deny access if user is superuser
        if request.user.is_superuser:
            messages.error(request,
                           mark_safe('Request denied.<br/>Superuser '
                                     'must contact our team for this action.'))
            return redirect(reverse('home'))
        messages.warning(request,
                         mark_safe("You're now tring to remove your account."
                                   "<br/>Please read our warning message "
                                   "before your leaving."))
        return render(
            request,
            "profiles/delete_account.html",
        )


class DeleteAction(LoginRequiredMixin, View):
    """ View to delete account after confirmation """

    def post(self, request):
        """ POST method """
        # deny access if user is superuser
        if request.user.is_superuser:
            messages.error(request,
                           mark_safe('Request denied.<br/>Superuser '
                                     'must contact our team for this action.'))
            return redirect(reverse('home'))
        try:
            request.user.delete()
            messages.success(request,
                             mark_safe('Thanks for join us.'
                                       'Hope to meet you again someday!'))
        # if user record not exist then raise the exception
        except ObjectDoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect(reverse('home'))
        # whatever the result redirect to home page
        return redirect(reverse('home'))


class OrderList(LoginRequiredMixin, generic.ListView):
    """ Show a table with list of Order review details """
    model = Order
    template_name = "profiles/order_list.html"

    def get(self, request, *args, **kwargs):
        """ GET method """
        # deny access if user is not superuser
        if not request.user.is_superuser:
            messages.error(request,
                           mark_safe('Request denied.<br/>'
                                     'Only admin can access.'))
            return redirect(reverse('home'))
        return super(OrderList, self).get(request, *args, **kwargs)
