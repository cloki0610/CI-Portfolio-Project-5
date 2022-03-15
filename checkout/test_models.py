""" Test models in checkout application """
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, Product
from .models import Order, OrderLineItem


class TestCheckoutModels(TestCase):
    """ Test Order and OrderLineItem models """

    def setUp(self):
        """Set up required instance """
        self.user = User.objects.create_user(
                    username='test',
                    password='password',
                    email='test@example.com')
        self.user.save()
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
        self.order = Order.objects.create(
            user_profile=self.user.userprofile,
        )
        self.order.save()
        self.lineitem = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3
        )
        self.lineitem.save()

    def test_order_string_method(self):
        """ Test string method and _generate_order_number """
        order = self.order
        self.assertNotEqual(str(order), '')

    def test_orderlineitem_string_method(self):
        """ Test string method """
        order = self.order
        lineitem = self.lineitem
        self.assertEqual(str(lineitem),
                         (f'SKU {lineitem.product.sku} on order'
                          f' {order.order_number}'))

    def test_post_save_signal(self):
        """
        Test post_save signal to update new totals when lineitem update
        """
        order = self.order
        self.assertEqual(order.order_total, 4.5)
        self.assertEqual(order.grand_total, Decimal('4.95'))
        lineitem = self.lineitem
        lineitem.quantity = 6
        lineitem.save()
        self.assertEqual(order.order_total, 9)
        self.assertEqual(order.grand_total, Decimal('9.9'))

    def test_post_delete_signal(self):
        """
        Test post_save signal to update new totals when lineitem delete
        """
        order = self.order
        self.assertEqual(order.order_total, 4.5)
        self.assertEqual(order.grand_total, Decimal('4.95'))
        lineitem = self.lineitem
        lineitem.delete()
        self.assertEqual(order.order_total, 0)
        self.assertEqual(order.grand_total, 0)
