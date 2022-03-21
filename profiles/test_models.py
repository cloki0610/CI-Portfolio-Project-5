""" Test models in profile application """
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class TestProductsModels(TestCase):
    """ Test Category and Product models """

    def setUp(self):
        """ Set up required instance """
        self.user = User.objects.create_user(
            username='test',
            password='password',
            email='test@example.com')
        self.user.save()

    def test_userprofile_string_method(self):
        """ Test string method output """
        userprofile = UserProfile.objects.get(user=1)
        self.assertEqual(str(userprofile), "test")

    def test_userprofile_postsave_signal(self):
        """ Test userprofile signal to auto create userprofile """
        new_user = User.objects.create_user(
            username='test2',
            password='password',
            email='test2@example.com')
        self.assertEqual(str(new_user.userprofile), "test2")
