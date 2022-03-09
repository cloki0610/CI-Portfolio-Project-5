""" View of profiles """
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserProfileForm


class ProfileView(LoginRequiredMixin, View):
    """ View to display and edit user profile """

    def get(self, request):
        """ GET method """
        profile = request.user.userprofile
        orders = profile.orders.all()
        profile_form = UserProfileForm(instance=request.user.userprofile)
        messages.info(request, 'When editing your profile, ' +
                      'please know that your Full name and email ' +
                      'are required.')
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
            print(profile_form.errors)
            messages.error(request,
                           'Updated Invalid, Edit and Try Again!')
        # redirect to profile page
        return redirect(reverse('profile'))


class DeleteAccount(LoginRequiredMixin, View):
    """ confirm page for delete account """

    def get(self, request):
        # return template for confirmation before delete
        """ get method """
        if request.user.is_superuser:
            messages.error(request, 'Request denied, superuser ' +
                           'should contact our team before remove account.')
            return redirect(reverse('home'))
        messages.warning(request,
                         'You\'re now tring to remove your account. ' +
                         'Please read our warning message before you leaving.')
        return render(
            request,
            "profiles/delete_account.html",
        )


class DeleteAction(LoginRequiredMixin, View):
    """ View to delete account after confirmation """

    def post(self, request):
        """ POST method """
        if request.user.is_superuser:
            messages.error(request, 'Request denied, superuser ' +
                           'should contact our team before remove account.')
            return redirect(reverse('home'))
        try:
            request.user.delete()
            messages.success(request,
                             'Thanks for join us and hope to see you again!')
        # if user record not exist then raise the exception
        except ObjectDoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect(reverse('home'))
        # whatever the result redirect to home page
        return redirect(reverse('home'))
