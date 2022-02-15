from django.shortcuts import render


def index(request):
    """ View to index page """
    return render(request, "home/index.html")
