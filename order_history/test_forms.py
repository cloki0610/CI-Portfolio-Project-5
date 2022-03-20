""" Test forms in order_history application """
from django.test import TestCase
from .forms import OrderReviewForm, CommentForm


class TestOrderReviewForms(TestCase):
    """ Test OrderReview, Comment form model """

    def test_orderreviewform_is_valid(self):
        """ Test order review form model with valid input """
        form = OrderReviewForm({
            'order_status': 0,
            'review': 'Test review content'
        })
        self.assertTrue(form.is_valid())

    def test_orderreviewform_order_status_is_required(self):
        """ Test order review form model with blank input """
        form = OrderReviewForm({
            'order_status': '',
            'review': 'Test review content'
        })
        self.assertFalse(form.is_valid())

    def test_orderreviewform_order_status_is_invalid(self):
        """ Test order review form model with invalid input """
        form = OrderReviewForm({
            'order_status': 6,
            'review': 'Test review content'
        })
        self.assertFalse(form.is_valid())

    def test_orderreviewform_review_is_required(self):
        """ Test order review form model with blank input """
        form = OrderReviewForm({
            'order_status': 0,
            'review': ''
        })
        self.assertFalse(form.is_valid())

    def test_commentform_is_valid(self):
        """ Test order review form model with valid input """
        form = CommentForm({
            'comment': 'Test comment text'
        })
        self.assertTrue(form.is_valid())

    def test_commentform_is_required(self):
        """ Test order review form model with blank input """
        form = CommentForm({
            'comment': ''
        })
        self.assertFalse(form.is_valid())
