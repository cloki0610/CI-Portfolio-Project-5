""" Test forms in products application """
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from .models import Category
from .forms import ProductForm


class TestProductsForms(TestCase):
    """ Test Product form model """

    def setUp(self):
        """Set up required instance """
        self.category = Category.objects.create(
            name='personal_items',
            friendly_name='Personal items'
        )
        self.category.save()
        self.testimage = SimpleUploadedFile(name='rs2850487.jpg', content=open(
            (settings.MEDIA_ROOT+'/rs2850487.jpg'), 'rb').read(),
            content_type='image/jpeg')

    def test_productform_is_valid(self):
        """ Test product form model with valid input """
        form = ProductForm({
            'category': self.category,
            'sku': 'rs2850487',
            'name': 'Knitted vest(L)',
            'description': ('A vest purchase from shop 2 years '
                            'ago but unused at last. Large size.'),
            'price': 70.0,
            'image_url': 'https://i.imgur.com/k08s8VS.jpg?1',
            'image': self.testimage
        })
        self.assertTrue(form.is_valid())

    def test_category_is_optional(self):
        """ Test with blank category input """
        form = ProductForm({
            'category': '',
            'sku': 'rs2850487',
            'name': 'Knitted vest(L)',
            'description': ('A vest purchase from shop 2 years '
                            'ago but unused at last. Large size.'),
            'price': 70.0,
            'image_url': 'https://i.imgur.com/k08s8VS.jpg?1',
            'image': self.testimage
        })
        self.assertTrue(form.is_valid())

    def test_sky_is_optional(self):
        """ Test with blank sku input """
        form = ProductForm({
            'category': self.category,
            'sku': '',
            'name': 'Knitted vest(L)',
            'description': ('A vest purchase from shop 2 years '
                            'ago but unused at last. Large size.'),
            'price': 70.0,
            'image_url': 'https://i.imgur.com/k08s8VS.jpg?1',
            'image': self.testimage
        })
        self.assertTrue(form.is_valid())

    def test_name_is_required(self):
        """ Test with blank name input """
        form = ProductForm({
            'category': self.category,
            'sku': 'rs2850487',
            'name': '',
            'description': ('A vest purchase from shop 2 years '
                            'ago but unused at last. Large size.'),
            'price': 70.0,
            'image_url': 'https://i.imgur.com/k08s8VS.jpg?1',
            'image': self.testimage
        })
        self.assertFalse(form.is_valid())

    def test_description_is_required(self):
        """ Test with blank description input """
        form = ProductForm({
            'category': self.category,
            'sku': 'rs2850487',
            'name': 'Knitted vest(L)',
            'description': '',
            'price': 70.0,
            'image_url': 'https://i.imgur.com/k08s8VS.jpg?1',
            'image': self.testimage
        })
        self.assertFalse(form.is_valid())

    def test_price_is_required(self):
        """ Test with blank price input """
        form = ProductForm({
            'category': self.category,
            'sku': 'rs2850487',
            'name': 'Knitted vest(L)',
            'description': ('A vest purchase from shop 2 years '
                            'ago but unused at last. Large size.'),
            'price': '',
            'image_url': 'https://i.imgur.com/k08s8VS.jpg?1',
            'image': self.testimage
        })
        self.assertFalse(form.is_valid())

    def test_image_url_is_optional(self):
        """ Test with blank image_url input """
        form = ProductForm({
            'category': self.category,
            'sku': 'rs2850487',
            'name': 'Knitted vest(L)',
            'description': ('A vest purchase from shop 2 years '
                            'ago but unused at last. Large size.'),
            'price': 70.0,
            'image_url': '',
            'image': self.testimage
        })
        self.assertTrue(form.is_valid())

    def test_image_is_optional(self):
        """ Test with blank image input """
        form = ProductForm({
            'category': self.category,
            'sku': 'rs2850487',
            'name': 'Knitted vest(L)',
            'description': ('A vest purchase from shop 2 years '
                            'ago but unused at last. Large size.'),
            'price': 70.0,
            'image_url': 'https://i.imgur.com/k08s8VS.jpg?1',
            'image': ''
        })
        self.assertTrue(form.is_valid())
