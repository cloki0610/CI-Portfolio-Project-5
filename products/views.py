""" Views of products """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category


class ProductsView(View):
    """ Display a full list of all products """

    def get(self, request):
        """ GET method """
        products = Product.objects.all().order_by('name')
        category = None
        query = None
        sort = None
        direction = None
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "Please enter a keyword for search")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query
                        ) | Q(description__icontains=query)
            products = products.filter(queries)
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        # use paginator to manage the result
        products_paginator = Paginator(products, 8)
        page_number = request.GET.get('page')
        products_page = products_paginator.get_page(page_number)

        # return data with template
        current_sort = f'{sort}_{direction}'
        return render(
            request,
            "products/products.html",
            {
                "products_page": products_page,
                "search_keyword": query,
                "category": category,
                "current_sort": current_sort
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
