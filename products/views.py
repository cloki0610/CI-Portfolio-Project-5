""" Views of products """
from django.shortcuts import (render, get_object_or_404,
                              HttpResponse, redirect, reverse)
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.functions import Lower
from django.utils.safestring import mark_safe
from .forms import ProductForm
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
        param = ""
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            param += f"&category={request.GET['category']}"
            products = products.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)
        if 'q' in request.GET:
            query = request.GET['q']
            param += f'&q={query}'
            if not query:
                messages.error(request,
                               "Please enter a keyword for search.")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query
                        ) | Q(description__icontains=query)
            products = products.filter(queries)
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            param += f'&sort={sortkey}'
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                param += f'&direction={direction}'
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
                "current_sort": current_sort,
                "param": param
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


class AddProductView(LoginRequiredMixin, View):
    """ A Form to add new product to database """

    def get(self, request):
        """ GET method """
        if not request.user.is_superuser:
            messages.error(request,
                           mark_safe('Request denied.<br/>'
                                     'Only admin can access.'))
            return redirect(reverse('home'))
        product_form = ProductForm()
        return render(
            request,
            "products/add_product.html",
            {
                "product_form": product_form
            }
        )

    def post(self, request):
        """ POST method """
        if not request.user.is_superuser:
            messages.error(request,
                           mark_safe('Request denied.<br/>'
                                     'Only admin can access.'))
            return redirect(reverse('home'))
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'New product added successfully.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           mark_safe('Action Failed.<br/>'
                                     'Check your form input and try again.'))
            return redirect(reverse('add_product'))


class EditProductView(LoginRequiredMixin, View):
    """ A Form to edit new product to database """

    def get(self, request, product_pk):
        """ GET method """
        if not request.user.is_superuser:
            messages.error(request,
                           mark_safe('Request denied.<br/>'
                                     'Only admin can access.'))
            return redirect(reverse('home'))
        product = get_object_or_404(Product, pk=product_pk)
        form = ProductForm(instance=product)
        messages.info(request, f'Now editing {product.name}.')

        return render(
            request,
            'products/edit_product.html', {
                'product_form': form,
                'product': product,
            })

    def post(self, request, product_pk):
        """ POST method """
        if not request.user.is_superuser:
            messages.error(request,
                           mark_safe('Request denied.<br/>'
                                     'Only admin can access.'))
            return redirect(reverse('home'))
        product = get_object_or_404(Product, pk=product_pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Update { product.name } successfully.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           mark_safe('Update Failed.<br/>'
                                     'Check your form input and try again.'))
            return redirect(reverse('edit_product', args=[product.id]))


class DeleteProductView(LoginRequiredMixin, View):
    """ A post method to remove product from database """

    def post(self, request, product_pk):
        """ POST method """
        if not request.user.is_superuser:
            messages.error(request,
                           mark_safe('Request denied.<br/>'
                                     'Only admin can access.'))
            return redirect(reverse('home'))
        product = get_object_or_404(Product, pk=product_pk)
        try:
            product.delete()
            messages.success(request, 'Selected product successfully removed.')
        except Exception as error:
            messages.error(request, f'Action Error: {error}')
            return HttpResponse(status=500)
        return redirect(reverse('products'))


class DeleteConfirmationView(LoginRequiredMixin, View):
    """ A confirm page before remove a product """

    def get(self, request, product_pk):
        """ GET method """
        if not request.user.is_superuser:
            messages.error(request,
                           mark_safe('Request denied.<br/>'
                                     'Only admin can access.'))
            return redirect(reverse('home'))
        product = get_object_or_404(Product, pk=product_pk)
        return render(request,
                      "products/delete_product_confirm.html", {
                          'product': product
                      })
