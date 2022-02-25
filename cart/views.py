from django.shortcuts import render


def view_cart(request):
    """ View to list all selected items """
    return render(request, "cart/cart.html")
