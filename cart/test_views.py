""" Test views in cart application """
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from products.models import Category, Product


class TestCartViews(TestCase):
    """ Cart Views test cases """

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

    def test_get_view_cart(self):
        """ Test GET method to render cart.html template """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_post_addtocartview(self):
        """ Test POST method in AddToCartView to add new item to context """
        response = self.client.post('/cart/add/1/', {
            'quantity': 3,
            'redirect_url': '/products/1/'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/1/')
        new_cart = self.client.session['cart']
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         (f'Added {new_cart[str(self.product.id)]}'
                          f' of {self.product.name} to your cart.'))

    def test_post_addtocartview_item_exist(self):
        """ Test POST method in AddToCartView to add exist item """
        session = self.client.session
        cart = {'1': 3}
        session['cart'] = cart
        session.save()
        response = self.client.post('/cart/add/1/', {
            'quantity': 3,
            'redirect_url': '/products/1/'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {'1': 6})
        self.assertRedirects(response, '/products/1/')
        new_cart = self.client.session['cart']
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         (f'Added {new_cart[str(self.product.id)]} '
                          f'of {self.product.name} to your cart.'))

    def test_post_updateitemview(self):
        """ Test POST method in UpdateItemView to update item in context """
        session = self.client.session
        cart = {'1': 3}
        session['cart'] = cart
        session.save()
        response = self.client.post('/cart/update/1/', {
            'quantity': 6
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {'1': 6})
        self.assertRedirects(response, '/cart/')
        new_cart = self.client.session['cart']
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         (f'Added {new_cart[str(self.product.id)]} '
                          f'of {self.product.name} to your cart.'))

    def test_post_updateitemview_remove_item(self):
        """
        Test POST method in UpdateItemView to remove item by set qty to 0
        """
        session = self.client.session
        cart = {'1': 3}
        session['cart'] = cart
        session.save()
        response = self.client.post('/cart/update/1/', {
            'quantity': 0
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {})
        self.assertRedirects(response, '/cart/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         (f'Removed {self.product.name} '
                          f'from your cart'))

    def test_post_removeitemview_remove_item(self):
        """
        Test POST method in RemoveItemView to remove item
        """
        session = self.client.session
        cart = {'1': 3}
        session['cart'] = cart
        session.save()
        response = self.client.post('/cart/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'], {})
        self.assertRedirects(response, '/cart/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Removed {self.product.name} from your cart')

    def test_post_removeitemview_remove_item_error(self):
        """
        Test POST method in RemoveItemView to remove item from empty cart
        """
        response = self.client.post('/cart/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/cart/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Error action: '1'")
