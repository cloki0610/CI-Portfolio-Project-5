""" Test models in about application """
from django.test import TestCase
from .models import Contact, NewsLetter


class TestAboutModels(TestCase):
    """ Test Contact and NewsLetter models """

    def setUp(self):
        """Set up required instance """
        self.contact = Contact.objects.create(
            name='Test',
            email='test@unittest.com',
            other_contact='3408446915',
            message='Test data for unit test'
        )
        self.contact.save()
        self.newsletter = NewsLetter.objects.create(
            email='test@unittest.com'
        )
        self.newsletter.save()

    def test_contact_string_method(self):
        """ Test string method output"""
        contact = self.contact
        self.assertEqual(str(contact), 'Message from Test')

    def test_newsletter_string_method(self):
        """ Test string method output """
        newsletter = self.newsletter
        self.assertEqual(str(newsletter), 'test@unittest.com')
