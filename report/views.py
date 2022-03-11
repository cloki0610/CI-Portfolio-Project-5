""" Views of report """
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator
from products.models import Product
from .forms import ReportForm
from .models import Report


class ReportView(View):
    """
    Display a  report form to annoymous quest
    to submit a form to report low quality product
    """

    def get(self, request, product_pk):
        """ GET method """
        report_form = ReportForm()
        product = get_object_or_404(Product, pk=product_pk)
        return render(
            request,
            "report/report.html", {
                "product": product,
                "report_form": report_form
            }
        )

    def post(self, request, product_pk):
        """ POST method """
        product = get_object_or_404(Product, pk=product_pk)
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.product = product
            report.save()
            messages.success(request,
                             'Sorry for your bad experience.' +
                             'We will do as much as we can ' +
                             'to solve the problem.')
        else:
            messages.error(request,
                           'Submit failed, Please check and Try Again!')
            return redirect(reverse('report', args=[product_pk]))
        return redirect(reverse('product_detail', args=[product_pk]))


class ReportListView(LoginRequiredMixin, View):
    """ Display a list of report to admin to check reports """

    def get(self, request):
        """ GET method """
        if not request.user.is_superuser:
            messages.error(request, 'Request denied, only admin can access.')
            return redirect(reverse('home'))
        reports = Report.objects.all().order_by('-report_on')
        report_paginator = Paginator(reports, 5)
        page_number = request.GET.get('page')
        report_page = report_paginator.get_page(page_number)

        return render(
            request,
            "report/report_list.html",
            {
                "report_page": report_page
            }
        )


class ReportChecked(LoginRequiredMixin, View):
    """ Toggle button to set report.checked to true of false """

    def post(self, request, report_id):
        """ POST method """
        if not request.user.is_superuser:
            messages.error(request, 'Request denied, only admin can access.')
            return redirect(reverse('home'))
        report = get_object_or_404(Report, pk=report_id)
        report.checked = not report.checked
        report.save()
        return redirect(reverse('report_list'))
