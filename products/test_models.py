""" Test models in product application """
from django.test import TestCase
from .models import Category, Product


class TestProductsModels(TestCase):
    """ Test Category and Product models """

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

    def test_category_string_method(self):
        """ Test string method output """
        category = self.category
        self.assertEqual(str(category), "personal_items")

    def test_category_get_friendly_name(self):
        """ Test get_friendly_name output """
        category = self.category
        self.assertEqual(category.get_friendly_name(), "Personal items")

    def test_product_string_method(self):
        """ Test string method output """
        product = self.product
        self.assertEqual(str(product), "Hand made chocolate eggs(12pcs)")
