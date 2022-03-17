""" Test forms in about application """
from django.test import TestCase
from .forms import ContactForm, NewsletterForm


class TestAboutForms(TestCase):
    """ Test Contact, NewsLetter form model """

    def test_contactform_is_valid(self):
        """ Test contact form model with valid input """
        form = ContactForm({
            'name': 'Test',
            'email': 'test@unittest.com',
            'other_contact': '3408446915',
            'message': 'Test data for unit test'
        })
        self.assertTrue(form.is_valid())

    def test_name_is_required(self):
        """ Test with blank name input """
        form = ContactForm({
            'name': '',
            'email': 'test@unittest.com',
            'other_contact': '3408446915',
            'message': 'Test data for unit test'
        })
        self.assertFalse(form.is_valid())

    def test_email_is_optional(self):
        """ Test with blank email input """
        form = ContactForm({
            'name': 'Test',
            'email': '',
            'other_contact': '3408446915',
            'message': 'Test data for unit test'
        })
        self.assertTrue(form.is_valid())

    def test_other_contact_is_optional(self):
        """ Test with blank other_contact input """
        form = ContactForm({
            'name': 'Test',
            'email': 'test@unittest.com',
            'other_contact': '',
            'message': 'Test data for unit test'
        })
        self.assertTrue(form.is_valid())

    def test_message_is_required(self):
        """ Test with blank message input """
        form = ContactForm({
            'name': 'Test',
            'email': 'test@unittest.com',
            'other_contact': '3408446915',
            'message': ''
        })
        self.assertFalse(form.is_valid())

    def test_newsletter_form_is_valid(self):
        """ Test newsletter form model with valid input """
        form = NewsletterForm({
            'email': 'test@unittest.com',
        })
        self.assertTrue(form.is_valid())

    def test_newsletter_form_is_invalid(self):
        """ Test newsletter form model with invalid input """
        form = NewsletterForm({
            'email': 'testinvalidinput',
        })
        self.assertFalse(form.is_valid())
