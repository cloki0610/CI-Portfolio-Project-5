""" Test forms in checkout application """
from django.test import TestCase
from .forms import OrderForm


class TestOrderForms(TestCase):
    """ Test Order form model """

    def test_form_is_valid(self):
        """ Test order form model with a valid input """
        form = OrderForm({
            'full_name': 'Test',
            'email': 'test@test.com',
            'phone_number': '79648565733',
            'postcode': 'T361AQ',
            'town_or_city': 'Test Only',
            'street_address1': 'Test street 1',
            'street_address2': 'Test address 2',
            'county': 'Test',
            'country': 'GB'
        })
        self.assertTrue(form.is_valid())

    def test_fullname_is_required(self):
        """ Test with blank full_name input """
        form = OrderForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': '79648565733',
            'postcode': 'T361AQ',
            'town_or_city': 'Test Only',
            'street_address1': 'Test street 1',
            'street_address2': 'Test address 2',
            'county': 'Test',
            'country': 'GB'
        })
        self.assertFalse(form.is_valid())

    def test_email_is_required(self):
        """ Test with blank email input """
        form = OrderForm({
            'full_name': 'Test',
            'email': '',
            'phone_number': '79648565733',
            'postcode': 'T361AQ',
            'town_or_city': 'Test Only',
            'street_address1': 'Test street 1',
            'street_address2': 'Test address 2',
            'county': 'Test',
            'country': 'GB'
        })
        self.assertFalse(form.is_valid())

    def test_phone_number_is_required(self):
        """ Test with blank phone_number input """
        form = OrderForm({
            'full_name': 'Test',
            'email': 'test@test.com',
            'phone_number': '',
            'postcode': 'T361AQ',
            'town_or_city': 'Test Only',
            'street_address1': 'Test street 1',
            'street_address2': 'Test address 2',
            'county': 'Test',
            'country': 'GB'
        })
        self.assertFalse(form.is_valid())

    def test_postcode_is_optional(self):
        """ Test with blank postcode input """
        form = OrderForm({
            'full_name': 'Test',
            'email': 'test@test.com',
            'phone_number': '79648565733',
            'postcode': '',
            'town_or_city': 'Test Only',
            'street_address1': 'Test street 1',
            'street_address2': 'Test address 2',
            'county': 'Test',
            'country': 'GB'
        })
        self.assertTrue(form.is_valid())

    def test_town_or_city_is_required(self):
        """ Test with blank town_or_city input """
        form = OrderForm({
            'full_name': 'Test',
            'email': 'test@test.com',
            'phone_number': '79648565733',
            'postcode': 'T361AQ',
            'town_or_city': '',
            'street_address1': 'Test street 1',
            'street_address2': 'Test address 2',
            'county': 'Test',
            'country': 'GB'
        })
        self.assertFalse(form.is_valid())

    def test_street_address1_is_required(self):
        """ Test with blank street_address1 input """
        form = OrderForm({
            'full_name': 'Test',
            'email': 'test@test.com',
            'phone_number': '79648565733',
            'postcode': 'T361AQ',
            'town_or_city': 'Test Only',
            'street_address1': '',
            'street_address2': 'Test address 2',
            'county': 'Test',
            'country': 'GB'
        })
        self.assertFalse(form.is_valid())

    def test_street_address2_is_optional(self):
        """ Test with blank street_address2 input """
        form = OrderForm({
            'full_name': 'Test',
            'email': 'test@test.com',
            'phone_number': '79648565733',
            'postcode': 'T361AQ',
            'town_or_city': 'Test Only',
            'street_address1': 'Test street 1',
            'street_address2': '',
            'county': 'Test',
            'country': 'GB'
        })
        self.assertTrue(form.is_valid())

    def test_county_is_optional(self):
        """ Test with blank county input """
        form = OrderForm({
            'full_name': 'Test',
            'email': 'test@test.com',
            'phone_number': '79648565733',
            'postcode': 'T361AQ',
            'town_or_city': 'Test Only',
            'street_address1': 'Test street 1',
            'street_address2': 'Test address 2',
            'county': '',
            'country': 'GB'
        })
        self.assertTrue(form.is_valid())

    def test_country_is_required(self):
        """ Test with blank country input """
        form = OrderForm({
            'full_name': 'Test',
            'email': 'test@test.com',
            'phone_number': '79648565733',
            'postcode': 'T361AQ',
            'town_or_city': 'Test Only',
            'street_address1': 'Test street 1',
            'street_address2': 'Test address 2',
            'county': 'Test',
            'country': ''
        })
        self.assertFalse(form.is_valid())
