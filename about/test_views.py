""" Test views in about application """
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.utils.safestring import mark_safe


class TestAboutViews(TestCase):
    """ About Views test cases """

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

    def test_get_about_view(self):
        """ Test GET method to render about.html template """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')

    def test_get_contact_view(self):
        """ Test GET method to render contact.html template """
        response = self.client.get('/about/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/contact.html')

    def test_post_contact_view(self):
        """ Test POST method to submit contact form """
        response = self.client.post('/about/contact/', {
            'name': 'Test',
            'email': 'test@unittest.com',
            'other_contact': '3408446915',
            'message': 'Test data for unit test'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Thank you for your support!')

    def test_get_contact_list_no_login(self):
        """
        Test GET method to render contact_list.html template without login
        """
        response = self.client.get('/about/contact_list/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/about/contact_list/')

    def test_get_contact_list_normal_user(self):
        """
        Test GET method to render contact_list.html template as user
        """
        self.client.login(username='test', password='password')
        response = self.client.get('/about/contact_list/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Request denied.<br/>'
                                   'Only admin can access.'))

    def test_get_contact_list_super_user(self):
        """
        Test GET method to render contact_list.html template as superuser
        """
        self.client.login(username='test_superuser', password='password')
        response = self.client.get('/about/contact_list/')
        self.assertEqual(response.status_code, 200)

    def test_get_newsletter_view(self):
        """ Test GET method to render newsletter.html template """
        response = self.client.get('/about/newsletter/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/newsletter.html')

    def test_post_newsletter_view(self):
        """ Test POST method to submit email to subscribe newsletter """
        response = self.client.post('/about/newsletter/', {
            'email': 'test@unittest.com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Thank you for your subscribion!')
