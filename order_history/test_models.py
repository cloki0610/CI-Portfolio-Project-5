""" Test models in order_history application """
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.text import slugify
from products.models import Category, Product
from checkout.models import Order, OrderLineItem
from .models import OrderReview, Comment


class TestOrderHistoryModels(TestCase):
    """ Test OrderReview and Comment models """

    def setUp(self):
        """Set up required instance """
        self.user = User.objects.create_user(
                    username='test',
                    password='password',
                    email='test@example.com')
        self.user.save()
        self.category = Category.objects.create(
            name='personal_items',
            friendly_name='Personal items'
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
            image="rs6625273.jpg"
        )
        self.product.save()
        self.order = Order.objects.create(
            user_profile=self.user.userprofile,
        )
        self.order.save()
        self.lineitem = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3
        )
        self.lineitem.save()
        self.orderreview = OrderReview.objects.create(
            order=self.order,
            customer=self.user.userprofile,
            order_status=0,
            review='Test review content'
        )
        self.orderreview.save()
        self.comment = Comment.objects.create(
            order_review=self.orderreview,
            user=self.user.userprofile,
            comment='Test comment'
        )
        self.comment.save()

    def test_orderreview_string_method(self):
        """ Test orderreview model string method output """
        orderreview = self.orderreview
        self.assertEqual(str(orderreview),
                         f"{str(self.user.userprofile)}-{str(self.order)}")

    def test_auto_generate_slug(self):
        """ Test save method to create the slug when save record """
        orderreview = self.orderreview
        self.assertEqual(orderreview.slug, slugify(orderreview))

    def test_comment_string_method(self):
        """ Test comment model string method output """
        comment = self.comment
        self.assertEqual(str(comment),
                         f"{str(self.user)} - Reply on {self.orderreview}")
