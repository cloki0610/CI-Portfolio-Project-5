""" View of profiles """
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import UserProfile


class ProfileView(View):
    """ View to display user profile """

    def get(self, request):
        """ GET method """
        profile = get_object_or_404(UserProfile, user=request.user)
        return render(request,
                      "profiles/profile.html",
                      {
                          'profile': profile,
                      })
