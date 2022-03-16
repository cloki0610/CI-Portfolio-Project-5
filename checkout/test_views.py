""" Test views in checkout application """
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.messages import get_messages
from products.models import Category, Product
from .models import Order, OrderLineItem


class TestCheckoutViews(TestCase):
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

    def test_get_checkoutview(self):
        """ Test CheckOutView GET method """
        session = self.client.session
        cart = {'1': 3}
        session['cart'] = cart
        session.save()
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_get_checkoutview_no_cart(self):
        """ Test CheckOutView GET method without cart"""
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("Your cart still empty.<br/>"
                                   "Please add some item before checkout."))

    def test_get_checkoutview_with_login(self):
        """ Test CheckOutView GET method with login """
        self.client.login(username='test', password='password')
        session = self.client.session
        cart = {'1': 3}
        session['cart'] = cart
        session.save()
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
