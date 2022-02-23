""" Views of products """
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from .models import Product


class ProductsView(View):
    """ Display a full list of all products """

    def get(self, request):
        """ GET method """
        all_products = Product.objects.all().order_by('name')
        # use paginator to manage the result
        products_paginator = Paginator(all_products, 8)
        page_number = request.GET.get('page')
        products_page = products_paginator.get_page(page_number)

        # return data with template
        return render(
            request,
            "products/products.html",
            {
                "products_page": products_page
            }
        )
