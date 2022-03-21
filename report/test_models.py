""" Test models in report application """
from django.test import TestCase
from products.models import Category, Product
from .models import Report


class TestReportModels(TestCase):
    """ Test Report model """

    def setUp(self):
        """ Set up required instance """
        self.category = Category.objects.create(
            name='personal_items',
            friendly_name='Personal items'
        )
        self.category.save()
        self.product = Product.objects.create(
            sku="rs6625273",
            name="Hand made chocolate eggs(12pcs)",
            description=("12 pieces of handmade chocolate "
                         "eggs with a special gift card."),
            price=1.5,
            category=self.category,
            image_url="https://i.imgur.com/Ucno1to.jpg",
            image="rs6625273.jpg"
        )
        self.product.save()
        self.report = Report.objects.create(
            name="Test",
            product=self.product,
            problem_type=0,
            problem_description="sting for unit test"
        )
        self.report.save()

    def test_report_string_method(self):
        """ Test string method output """
        report = self.report
        self.assertEqual(str(report),
                         "Report of Hand made chocolate eggs(12pcs)")
