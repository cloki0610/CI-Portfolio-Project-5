""" Test views in profiles application """
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.utils.safestring import mark_safe


class TestProfileViews(TestCase):
    """ profiles Views test cases """

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

    def test_get_profilesview_without_login(self):
        """
        Test GET method to render profile.html template without login
        """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profile/')

    def test_get_profilesview(self):
        """ Test GET method to render profile.html template as user """
        self.client.login(username='test', password='password')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_post_profilesview_without_login(self):
        """
        Test POST method to submit form to update profile without login
        """
        response = self.client.post('/profile/', {
            'first_name': 'Unit',
            'last_name': 'Test',
            'email': 'test@unittest.com',
            'default_phone_number': '8677528333',
            'default_postcode': 'E3NA2',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '14, testing',
            'default_street_address2': 'test',
            'default_county': 'test',
            'default_country': 'GB'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profile/')

    def test_post_profilesview(self):
        """
        Test POST method to submit form to update profile as user
        """
        self.client.login(username='test', password='password')
        response = self.client.post('/profile/', {
            'first_name': 'Unit',
            'last_name': 'Test',
            'email': 'test@unittest.com',
            'default_phone_number': '8677528333',
            'default_postcode': 'E3NA2',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '14, testing',
            'default_street_address2': 'test',
            'default_county': 'test',
            'default_country': 'GB'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Your Profile Has Updated.')

    def test_post_profilesview_invalid_input(self):
        """
        Test POST method to submit form to update profile with invalid input
        """
        self.client.login(username='test', password='password')
        response = self.client.post('/profile/', {
            'first_name': '',
            'last_name': 'Test',
            'email': 'test@unittest.com',
            'default_phone_number': '8677528333',
            'default_postcode': 'E3NA2',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '14, testing',
            'default_street_address2': 'test',
            'default_county': 'test',
            'default_country': 'GB'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Updated Invalid.<br/>'
                                   'Please check and try again!'))

    def test_get_delete_account_without_login(self):
        """
        Test GET method to render delete_account.html template without login
        """
        response = self.client.get('/profile/delete_account/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profile/delete_account/')

    def test_get_delete_account(self):
        """ Test GET method to render delete_account.html template as user """
        self.client.login(username='test', password='password')
        response = self.client.get('/profile/delete_account/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/delete_account.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("You're now tring to remove your account."
                                   "<br/>Please read our warning message "
                                   "before your leaving."))

    def test_get_delete_account_superuser(self):
        """
        Test GET method to render delete_account.html template as superuser
        """
        self.client.login(username='test_superuser', password='password')
        response = self.client.get('/profile/delete_account/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>Superuser '
                                   'must contact our team for this action.'))

    def test_post_delete_action_without_login(self):
        """ Test POST method to delete user account without login """
        response = self.client.post('/profile/delete_action/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profile/delete_action/')

    def test_post_delete_action(self):
        """ Test POST method to delete user account as user """
        self.client.login(username='test', password='password')
        response = self.client.post('/profile/delete_action/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Thanks for join us.'
                                   'Hope to meet you again someday!'))

    def test_post_delete_action_superuser(self):
        """ Test POST method to delete user account as superuser """
        self.client.login(username='test_superuser', password='password')
        response = self.client.post('/profile/delete_action/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>Superuser '
                                   'must contact our team for this action.'))

    def test_get_order_list_without_login(self):
        """
        Test GET method to render order_list.html template without login
        """
        response = self.client.get('/profile/order/list/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profile/order/list/')

    def test_get_order_list_user(self):
        """
        Test GET method to render order_list.html template as user
        """
        self.client.login(username='test', password='password')
        response = self.client.get('/profile/order/list/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>'
                                   'Only admin can access.'))

    def test_get_order_list_superuser(self):
        """
        Test GET method to render order_list.html template as superuser
        """
        self.client.login(username='test_superuser', password='password')
        response = self.client.get('/profile/order/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/order_list.html')
