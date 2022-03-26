""" Test views in report application """
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.utils.safestring import mark_safe
from products.models import Category, Product
from .models import Report


class TestReportViews(TestCase):
    """ Report Views test cases """

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
        self.product.save()
        self.report = Report.objects.create(
            name='Test',
            product=self.product,
            problem_type=0,
            problem_description='text for testing'
        )
        self.report.save()

    def test_get_report_view(self):
        """ Test GET method to render products.html template """
        response = self.client.get('/report/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/report.html')

    def test_post_report_view(self):
        """ Test POST method to submit form for report product """
        response = self.client.post('/report/1/', {
            'name': 'Test',
            'problem_type': 0,
            'problem_description': 'string for testing reportform',
            'contact_email': 'test@unittest.com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Sorry for your bad experience.<br/>'
                                   'We will do as much as we can '
                                   'to solve the problem.'))

    def test_post_report_view_invalid_input(self):
        """
        Test POST method to submit form for report product with invalid input
        """
        response = self.client.post('/report/1/', {
            'name': '',
            'problem_type': 0,
            'problem_description': 'string for testing reportform',
            'contact_email': 'test@unittest.com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/report/1/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Invalid Input.<br/>'
                                   'Please check and Try Again!'))

    def test_get_report_list_view_without_login(self):
        """
        Test method to render report_list.html without login
        """
        response = self.client.get('/report/report_list/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/report/report_list/')

    def test_get_report_list_view_user(self):
        """
        Test method to render report_list.html as user
        """
        self.client.login(username='test', password='password')
        response = self.client.get('/report/report_list/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>'
                                   'Only admin can access.'))

    def test_get_report_list_view_superuser(self):
        """ Test POST method to render report_list.html as superuser """
        self.client.login(username='test_superuser', password='password')
        response = self.client.get('/report/report_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/report_list.html')

    def test_post_report_checked_view_without_login(self):
        """
        Test POST method to toggle checked value without login
        """
        response = self.client.post('/report/report_list/1/checked/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/accounts/login/?next='
                              '/report/report_list/1/checked/'))

    def test_post_report_checked_view_user(self):
        """ Test POST method to toggle checked value as user """
        self.client.login(username='test', password='password')
        response = self.client.post('/report/report_list/1/checked/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>'
                                   'Only admin can access.'))

    def test_post_report_checked_view_superuser(self):
        """ Test POST method to toggle checked value as superuser """
        self.client.login(username='test_superuser', password='password')
        response = self.client.post('/report/report_list/1/checked/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/report/report_list/')
