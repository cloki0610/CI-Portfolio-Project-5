""" Test forms in profile application """
from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserProfileForm


class TestUserProfileForms(TestCase):
    """ Test UserProfile form model """

    def setUp(self):
        """ Set up required instance """
        self.user = User.objects.create_user(
            username='test',
            password='password',
            email='test@example.com')
        self.user.save()

    def test_userprofileform_is_valid(self):
        """ Test userprofile form model with valid input """
        form = UserProfileForm({
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
        }, instance=self.user.userprofile)
        self.assertTrue(form.is_valid())

    def test_first_name_is_required(self):
        """ Test with blank first_name input """
        form = UserProfileForm({
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
        }, instance=self.user.userprofile)
        self.assertFalse(form.is_valid())

    def test_last_name_is_required(self):
        """ Test with blank last_name input """
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': '',
            'email': 'test@unittest.com',
            'default_phone_number': '8677528333',
            'default_postcode': 'E3NA2',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '14, testing',
            'default_street_address2': 'test',
            'default_county': 'test',
            'default_country': 'GB'
        }, instance=self.user.userprofile)
        self.assertFalse(form.is_valid())

    def test_email_is_required(self):
        """ Test with blank email input """
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'Test',
            'email': '',
            'default_phone_number': '8677528333',
            'default_postcode': 'E3NA2',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '14, testing',
            'default_street_address2': 'test',
            'default_county': 'test',
            'default_country': 'GB'
        }, instance=self.user.userprofile)
        self.assertFalse(form.is_valid())

    def test_default_phone_number_is_optional(self):
        """ Test with blank default_phone_number input """
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@unittest.com',
            'default_phone_number': '',
            'default_postcode': 'E3NA2',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '14, testing',
            'default_street_address2': 'test',
            'default_county': 'test',
            'default_country': 'GB'
        }, instance=self.user.userprofile)
        self.assertTrue(form.is_valid())

    def test_default_postcode_is_optional(self):
        """ Test with blank default_postcode input """
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@unittest.com',
            'default_phone_number': '8677528333',
            'default_postcode': '',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '14, testing',
            'default_street_address2': 'test',
            'default_county': 'test',
            'default_country': 'GB'
        }, instance=self.user.userprofile)
        self.assertTrue(form.is_valid())

    def test_default_town_or_city_is_optional(self):
        """ Test with blank default_town_or_city input """
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@unittest.com',
            'default_phone_number': '8677528333',
            'default_postcode': 'E3NA2',
            'default_town_or_city': '',
            'default_street_address1': '14, testing',
            'default_street_address2': 'test',
            'default_county': 'test',
            'default_country': 'GB'
        }, instance=self.user.userprofile)
        self.assertTrue(form.is_valid())

    def test_default_street_address1_is_optional(self):
        """ Test with blank default_street_address1 input """
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@unittest.com',
            'default_phone_number': '8677528333',
            'default_postcode': 'E3NA2',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '',
            'default_street_address2': 'test',
            'default_county': 'test',
            'default_country': 'GB'
        }, instance=self.user.userprofile)
        self.assertTrue(form.is_valid())

    def test_default_street_address2_is_optional(self):
        """ Test with blank default_street_address2 input """
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@unittest.com',
            'default_phone_number': '8677528333',
            'default_postcode': 'E3NA2',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '14, testing',
            'default_street_address2': '',
            'default_county': 'test',
            'default_country': 'GB'
        }, instance=self.user.userprofile)
        self.assertTrue(form.is_valid())

    def test_default_county_is_optional(self):
        """ Test with blank default_county input """
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@unittest.com',
            'default_phone_number': '8677528333',
            'default_postcode': 'E3NA2',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '14, testing',
            'default_street_address2': 'test',
            'default_county': '',
            'default_country': 'GB'
        }, instance=self.user.userprofile)
        self.assertTrue(form.is_valid())

    def test_default_country_is_optional(self):
        """ Test with blank default_country input """
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'test@unittest.com',
            'default_phone_number': '8677528333',
            'default_postcode': 'E3NA2',
            'default_town_or_city': 'Testing town',
            'default_street_address1': '14, testing',
            'default_street_address2': 'test',
            'default_county': 'test',
            'default_country': ''
        }, instance=self.user.userprofile)
        self.assertTrue(form.is_valid())
