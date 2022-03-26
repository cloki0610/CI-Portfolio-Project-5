""" Test view in Home application """
from django.test import TestCase
from django.contrib.auth.models import User


class TestHomeView(TestCase):
    """ Test home apps views """
    def setUp(self):
        """ Set up required instance """
        self.user = User.objects.create_user(
                    username='test',
                    password='password',
                    email='test@example.com')
        self.user.save()

    def test_get_index(self):
        """ Test get method to render index.html template """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_index_with_login(self):
        """ Test get method to render index.html template with login """
        self.client.login(username='test', password='password')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_error_404(self):
        """ Test an invalid path to error 404 page """
        response = self.client.get('/invalidurl')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
