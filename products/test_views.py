""" Test views in products application """
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.utils.safestring import mark_safe
from .models import Category, Product


class TestProductsViews(TestCase):
    """ order_history Views test cases """

    def setUp(self):
        """Set up required instance """
        self.user = User.objects.create_user(
            username='test',
            password='password',
            email='test@example.com')
        self.test_superuser = User.objects.create_superuser(
            username='test_superuser',
            password='password',
            email='testadmin@example.com')
        self.user.save()
        self.test_superuser.save()
        self.category = Category.objects.create(
            name='handmade',
            friendly_name='Handmade product'
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
            image=''
        )
        self.product2 = Product.objects.create(
            sku="rs6341572",
            name="Handmade chocolate cake",
            description=("A 6\" handmade chocolate cake with some "
                         "customer details if you need, delivery in UK only."),
            price=12.0,
            category=self.category,
            image_url="https://i.imgur.com/4NY1Qhe.jpg?1",
            image=''
        )
        self.product3 = Product.objects.create(
            sku="rs0266706",
            name="Handmade cookies(12pcs)",
            description=("12pcs of handmade cookies. You can also "
                         "require a gift card but it is optional."),
            price=2.0,
            category=self.category,
            image_url="https://i.imgur.com/DHF14ZO.jpg?1",
            image=''
        )
        self.product.save()
        self.product2.save()
        self.product3.save()

    def test_get_productsview(self):
        """ Test GET method to render products.html template """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_productsview_filter_by_category(self):
        """
        Test GET method to render template with category parameter
        """
        response = self.client.get('/products/?category=handmade')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['category'][0].name,
                         'handmade')
        self.assertEqual(str(response.context['products_page'].object_list[0]),
                         'Hand made chocolate eggs(12pcs)')
        self.assertEqual(response.context['param'], '&category=handmade')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_productsview_with_search_keyword(self):
        """
        Test GET method to render template with q parameter
        """
        response = self.client.get('/products/?q=eggs')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['search_keyword'],
                         'eggs')
        self.assertEqual(str(response.context['products_page'].object_list[0]),
                         'Hand made chocolate eggs(12pcs)')
        self.assertEqual(response.context['param'], '&q=eggs')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_productsview_with_sort(self):
        """
        Test GET method to render template with sort parameter
        """
        response = self.client.get('/products/?sort=price&direction=asc')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['current_sort'], 'price_asc')
        self.assertEqual(str(response.context['products_page'].object_list[0]),
                         'Hand made chocolate eggs(12pcs)')
        self.assertEqual(str(response.context['products_page'].object_list[1]),
                         'Handmade cookies(12pcs)')
        self.assertEqual(str(response.context['products_page'].object_list[2]),
                         'Handmade chocolate cake')
        self.assertEqual(response.context['param'],
                         '&sort=price&direction=asc')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_productdetailview(self):
        """
        Test GET method to render product_detail.html template
        """
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_get_add_product_view_without_login(self):
        """
        Test GET method to render add_product.html template without login
        """
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/products/add/')

    def test_get_add_product_view_user(self):
        """
        Test GET method to render add_product.html template as user
        """
        self.client.login(username='test', password='password')
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>'
                                   'Only admin can access.'))

    def test_get_add_product_view_superuser(self):
        """
        Test GET method to render add_product.html template as superuser
        """
        self.client.login(username='test_superuser', password='password')
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_post_add_product_view_without_login(self):
        """
        Test POST method to submit a form to add new product without login
        """
        response = self.client.post('/products/add/', {
            'category': self.category,
            'sku': 'rs2850487',
            'name': 'Knitted vest(L)',
            'description': ('A vest purchase from shop 2 years '
                            'ago but unused at last. Large size.'),
            'price': 70.0,
            'image_url': 'https://i.imgur.com/k08s8VS.jpg?1',
            'image': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/products/add/')

    def test_post_add_product_view_user(self):
        """
        Test POST method to submit a form to add new product as user
        """
        self.client.login(username='test', password='password')
        response = self.client.post('/products/add/', {
            'category': self.category,
            'sku': 'rs2850487',
            'name': 'Knitted vest(L)',
            'description': ('A vest purchase from shop 2 years '
                            'ago but unused at last. Large size.'),
            'price': 70.0,
            'image_url': 'https://i.imgur.com/k08s8VS.jpg?1',
            'image': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>'
                                   'Only admin can access.'))

    def test_post_add_product_view_superuser(self):
        """
        Test POST method to submit a form to add new product as superuser
        """
        self.client.login(username='test_superuser', password='password')
        response = self.client.post('/products/add/', {
            'category': '',
            'sku': 'rs2850487',
            'name': 'Knitted vest(L)',
            'description': ('A vest purchase from shop 2 years '
                            'ago but unused at last. Large size.'),
            'price': 70.0,
            'image_url': '',
            'image': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/4/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'New product added successfully.')

    def test_post_add_product_view_invalid_input(self):
        """
        Test POST method to submit a form to add new product with invalid input
        """
        self.client.login(username='test_superuser', password='password')
        response = self.client.post('/products/add/', {
            'category': self.category,
            'sku': 'rs2850487',
            'name': 'Knitted vest(L)',
            'description': '',
            'price': 70.0,
            'image_url': 'https://i.imgur.com/k08s8VS.jpg?1',
            'image': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Action Failed.<br/>'
                                   'Check your form input and try again.'))

    def test_get_edit_product_view_without_login(self):
        """
        Test GET method to render edit_product.html template without login
        """
        response = self.client.get('/products/edit/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/products/edit/1/')

    def test_get_edit_product_view_user(self):
        """
        Test GET method to render edit_product.html template as user
        """
        self.client.login(username='test', password='password')
        response = self.client.get('/products/edit/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>'
                                   'Only admin can access.'))

    def test_get_edit_product_view_superuser(self):
        """
        Test GET method to render edit_product.html template as superuser
        """
        self.client.login(username='test_superuser', password='password')
        response = self.client.get('/products/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Now editing {self.product.name}.')

    def test_post_edit_product_view_without_login(self):
        """
        Test POST method to submit a form to update product without login
        """
        response = self.client.post('/products/edit/1/', {
            'category': self.category,
            'sku': 'rs6625273',
            'name': 'Hand made chocolate eggs(12pcs)',
            'description': ("12 pieces of handmade chocolate "
                            "eggs with a special gift card."),
            'price': 1.5,
            'image_url': '',
            'image': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/products/edit/1/')

    def test_post_edit_product_view_user(self):
        """
        Test POST method to submit a form to update product as user
        """
        self.client.login(username='test', password='password')
        response = self.client.post('/products/edit/1/', {
            'category': self.category,
            'sku': 'rs6625273',
            'name': 'Hand made chocolate eggs(12pcs)',
            'description': ("12 pieces of handmade chocolate "
                            "eggs with a special gift card."),
            'price': 1.5,
            'image_url': '',
            'image': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>'
                                   'Only admin can access.'))

    def test_post_edit_product_view_superuser(self):
        """
        Test POST method to submit a form to update product as superuser
        """
        self.client.login(username='test_superuser', password='password')
        response = self.client.post('/products/edit/1/', {
            'category': '',
            'sku': 'rs6625273',
            'name': 'Hand made chocolate eggs(12pcs)',
            'description': ("12 pieces of handmade chocolate "
                            "eggs with a special gift card."),
            'price': 1.5,
            'image_url': '',
            'image': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         ('Update Hand made chocolate eggs'
                          '(12pcs) successfully.'))

    def test_post_edit_product_view_invalid_input(self):
        """
        Test POST method to submit a form to update product with invalid input
        """
        self.client.login(username='test_superuser', password='password')
        response = self.client.post('/products/edit/1/', {
            'category': self.category,
            'sku': 'rs6625273',
            'name': '',
            'description': ("12 pieces of handmade chocolate "
                            "eggs with a special gift card."),
            'price': 1.5,
            'image_url': '',
            'image': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/edit/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Update Failed.<br/>'
                                   'Check your form input and try again.'))

    def test_post_delete_product_view_without_login(self):
        """ Test POST method to delete a product without login """
        response = self.client.post('/products/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/products/delete/1/')

    def test_post_delete_product_view_user(self):
        """ Test POST method to delete a product as user """
        self.client.login(username='test', password='password')
        response = self.client.post('/products/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>'
                                   'Only admin can access.'))

    def test_post_delete_product_view_superuser(self):
        """ Test POST method to delete a product as superuser """
        self.client.login(username='test_superuser', password='password')
        response = self.client.post('/products/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Selected product successfully removed.')

    def test_get_delete_confirm_view_without_login(self):
        """
        Test GET method to render delete_product_confirm.html
        template without login
        """
        response = self.client.get('/products/delete_confirm/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/accounts/login/?next='
                              '/products/delete_confirm/1/'))

    def test_get_delete_confirm_view_user(self):
        """
        Test GET method to render delete_product_confirm.html
        template as user
        """
        self.client.login(username='test', password='password')
        response = self.client.get('/products/delete_confirm/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>'
                                   'Only admin can access.'))

    def test_get_delete_confirm_view_superuser(self):
        """
        Test GET method to render delete_product_confirm.html
        template as superuser
        """
        self.client.login(username='test_superuser', password='password')
        response = self.client.get('/products/delete_confirm/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/delete_product_confirm.html')
