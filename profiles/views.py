""" View of profiles """
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserProfileForm


class ProfileView(LoginRequiredMixin, View):
    """ View to display and edit user profile """

    def get(self, request):
        """ GET method """
        profile = request.user.userprofile
        orders = profile.orders.all()
        profile_form = UserProfileForm(instance=request.user.userprofile)
        return render(request,
                      "profiles/profile.html",
                      {
                          'profile_form': profile_form,
                          'orders': orders
                      })

    def post(self, request):
        """ POST method """
        profile_form = UserProfileForm(request.POST,
                                       request.FILES,
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
