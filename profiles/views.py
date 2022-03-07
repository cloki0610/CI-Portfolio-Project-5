""" View of profiles """
from django.shortcuts import render
from django.views import View
from django.contrib import messages


class ProfileView(View):
    """ View to display user profile """

    def get(self, request):
        """ GET method """
        return render(request,
                      "profiles/profile.html",
                      {})
