""" Views of products """
from django.shortcuts import render, get_object_or_404
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


class ProductDetailView(View):
    """ Display detail of specific product """

    def get(self, request, product_pk):
        """ GET method """
        product = get_object_or_404(Product, pk=product_pk)
        return render(
            request,
            "products/product_detail.html",
            {
                "product": product
            }
        )
