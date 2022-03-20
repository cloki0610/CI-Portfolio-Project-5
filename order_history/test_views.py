""" Test views in order_history application """
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from products.models import Category, Product
from checkout.models import Order, OrderLineItem
from .models import OrderReview, Comment


class TesOrderHistoryViews(TestCase):
    """ order_history Views test cases """

    def setUp(self):
        """Set up required instance """
        self.user = User.objects.create_user(
            username='test',
            password='password',
            email='test@example.com')
        self.user2 = User.objects.create_user(
            username='test2',
            password='password',
            email='test@example.com')
        self.test_superuser = User.objects.create_superuser(
            username='test_superuser',
            password='password',
            email='testadmin@example.com')
        self.user.save()
        self.user2.save()
        self.test_superuser.save()
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
        self.order2 = Order.objects.create(
            user_profile=self.user2.userprofile,
        )
        self.order.save()
        self.lineitem = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3
        )
        self.lineitem.save()
        self.lineitem2 = OrderLineItem.objects.create(
            order=self.order2,
            product=self.product,
            quantity=6
        )
        self.lineitem2.save()
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

    def test_get_orderhistoryview_without_login(self):
        """
        Test GET method to render order_history.html template without login
        """
        order = self.order
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profile/' +
                             f'order_history/{order.order_number}/')

    def test_get_orderhistoryview_valid_user(self):
        """
        Test GET method to render order_history.html template with valid user
        """
        order = self.order
        self.client.login(username='test', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_history/order_history.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('This is our record of '
                                   'your previous order(Ref. '
                                   f'{order.order_number}).'
                                   '<br/>Confirmation email should be sent '
                                   'on the order date.'))

    def test_get_orderhistoryview_invalid_user(self):
        """
        Test GET method to render order_history.html template with invalid user
        """
        order = self.order
        self.client.login(username='test2', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("Access Denied.<br/>"
                                   "Only order owner and admin "
                                   "can read this record."))

    def test_get_orderhistoryview_superuser(self):
        """
        Test GET method to render order_history.html template with superuser
        """
        order = self.order
        self.client.login(username='test_superuser', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_history/order_history.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('This is our record of '
                                   'your previous order(Ref. '
                                   f'{order.order_number}).'
                                   '<br/>Confirmation email should be sent '
                                   'on the order date.'))

    def test_get_orderreviewview_without_login(self):
        """
        Test GET method to render order_review.html template without login
        """
        order = self.order
        orderreview = self.orderreview
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'
                                    f'{orderreview.slug}/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profile/' +
                             f'order_history/{order.order_number}/'
                             f'{orderreview.slug}/')

    def test_get_orderreviewview_valid_user(self):
        """
        Test GET method to render order_review.html template with valid user
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'
                                    f'{orderreview.slug}/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_history/order_review.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('This is a review of '
                                   'your previous order(Ref. '
                                   f'{order.order_number}).'
                                   '<br/>Feel free to update or reply '
                                   'your review on the order date.'))

    def test_get_orderreviewview_invalid_user(self):
        """
        Test GET method to render order_review.html template with invalid user
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test2', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'
                                    f'{orderreview.slug}/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("Access Denied.<br/>"
                                   "Only order owner and admin "
                                   "can read this record."))

    def test_get_orderreviewview_superuser(self):
        """
        Test GET method to render order_review.html template with superuser
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test_superuser', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'
                                    f'{orderreview.slug}/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_history/order_review.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('This is a review of '
                                   'your previous order(Ref. '
                                   f'{order.order_number}).'
                                   '<br/>Feel free to update or reply '
                                   'your review on the order date.'))

    def test_get_orderreviewview_when_no_record(self):
        """
        Test GET method to render order_review.html template when no record
        """
        order = self.order2
        slug = slugify(f"{str(self.user2)}-{str(order)}")
        self.client.login(username='test2', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'
                                    f'{slug}/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/profile/order_history/'
                             f'{order.order_number}/create/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("You do not write any review yet.<br/>"
                                   "But we're welcome to know something "
                                   "about your previous order"))

    def test_get_orderreviewview_when_no_record_superuser(self):
        """
        Test GET method to render order_review.html template
        when user is superuser and no record
        """
        order = self.order2
        slug = slugify(f"{str(self.user2)}-{str(order)}")
        self.client.login(username='test_superuser', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'
                                    f'{slug}/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/order/list/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Error: User do not write any review yet.")

    def test_post_orderreviewview_without_login(self):
        """
        Test POST method to submit a comment form without login
        """
        order = self.order
        orderreview = self.orderreview
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/'), {
            'comment': 'Test comment text'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/accounts/login/?next=/'
                              'profile/order_history/'
                              f'{order.order_number}/'
                              f'{orderreview.slug}/'))

    def test_post_orderreviewview_valid_user(self):
        """
        Test POST method to submit a comment form as valid user
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/'), {
            'comment': 'Test comment text'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/profile/order_history/'
                              f'{order.order_number}/'
                              f'{orderreview.slug}/'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Reply on {order.order_number} successfully.')

    def test_post_orderreviewview_invalid_user(self):
        """
        Test POST method to submit a comment form as invalid user
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test2', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/'), {
            'comment': 'Test comment text'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("Access Denied.<br/>"
                                   "Only order owner and admin "
                                   "can read this record."))

    def test_post_orderreviewview_superuser(self):
        """
        Test POST method to submit a comment form as superuser
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test_superuser', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/'), {
            'comment': 'Test comment text'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/profile/order_history/'
                              f'{order.order_number}/'
                              f'{orderreview.slug}/'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Reply on {order.order_number} successfully.')

    def test_post_orderreviewview_input_invalid(self):
        """
        Test POST method to submit a comment form with invalid form
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/'), {
            'comment': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/profile/order_history/'
                              f'{order.order_number}/'
                              f'{orderreview.slug}/'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Invalid Input.<br/>'
                                   'Please check and try again.'))

    def test_get_createview_without_login(self):
        """
        Test GET method to render create_review.html template without login
        """
        order = self.order
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/create/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/accounts/login/?next=/profile/'
                              f'order_history/{order.order_number}/create/'))

    def test_get_createview_valid_user(self):
        """
        Test GET method to render create_review.html template as valid user
        """
        order = self.order
        self.client.login(username='test', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/create/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_history/create_review.html')

    def test_get_createview_invalid_user(self):
        """
        Test GET method to render create_review.html template as invalid user
        """
        order = self.order
        self.client.login(username='test2', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/create/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("Access Denied.<br/>"
                                   "Only order owner and admin "
                                   "can do this action."))

    def test_get_createview_superuser(self):
        """
        Test GET method to render create_review.html template as superuser
        """
        order = self.order
        self.client.login(username='test_superuser', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/create/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_history/create_review.html')

    def test_post_createview_without_login(self):
        """
        Test POST method to submit a new review record without login
        """
        order = self.order
        response = self.client.post(('/profile/order_history/'
                                    f'{order.order_number}/create/'), {
            'order_status': 0,
            'review': 'Test review content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/accounts/login/?next=/profile/'
                              f'order_history/{order.order_number}/create/'))

    def test_post_createview_valid_user(self):
        """
        Test POST method to submit a new review record as valid user
        """
        order = self.order2
        slug = slugify(f"{str(self.user2)}-{str(order)}")
        self.client.login(username='test2', password='password')
        response = self.client.post(('/profile/order_history/'
                                    f'{order.order_number}/create/'), {
            'order_status': 0,
            'review': 'Test review content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/profile/order_history/'
                              f'{order.order_number}/'
                              f'{slug}/'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Review Created.<br/>'
                                   'Thank you your support.<br/>'
                                   'If you need any help '
                                   'we will reply soon!'))

    def test_post_createview_invalid_user(self):
        """
        Test POST method to submit a new review record as invalid user
        """
        order = self.order2
        self.client.login(username='test', password='password')
        response = self.client.post(('/profile/order_history/'
                                    f'{order.order_number}/create/'), {
            'order_status': 0,
            'review': 'Test review content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("Access Denied.<br/>"
                                   "Only order owner and admin "
                                   "can do this action."))

    def test_post_createview_superuser(self):
        """
        Test POST method to submit a new review record as superuser
        """
        order = self.order2
        slug = slugify(f"{str(self.user2)}-{str(order)}")
        self.client.login(username='test_superuser', password='password')
        response = self.client.post(('/profile/order_history/'
                                    f'{order.order_number}/create/'), {
            'order_status': 0,
            'review': 'Test review content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/profile/order_history/'
                              f'{order.order_number}/'
                              f'{slug}/'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Review Created.<br/>'
                                   'Thank you your support.<br/>'
                                   'If you need any help '
                                   'we will reply soon!'))

    def test_post_createview_invalid_input(self):
        """
        Test POST method to submit a new review record with invalid input
        """
        order = self.order2
        self.client.login(username='test2', password='password')
        response = self.client.post(('/profile/order_history/'
                                    f'{order.order_number}/create/'), {
            'order_status': 6,
            'review': 'Test review content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Invalid Input.<br/>'
                                   'Please check your input and try again!'))

    def test_get_updateorderreview_without_login(self):
        """
        Test GET method to render update_review.html template without login
        """
        order = self.order
        orderreview = self.orderreview
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'
                                    f'{orderreview.slug}/update/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profile/' +
                             f'order_history/{order.order_number}/'
                             f'{orderreview.slug}/update/')

    def test_get_updateorderreview_valid_user(self):
        """
        Test GET method to render update_review.html template as valid user
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'
                                    f'{orderreview.slug}/update/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_history/update_review.html')

    def test_get_updateorderreview_invalid_user(self):
        """
        Test GET method to render update_review.html template as invalid user
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test2', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'
                                    f'{orderreview.slug}/update/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("Access Denied.<br/>"
                                   "Only order owner and admin "
                                   "can do this action."))

    def test_get_updateorderreview_superuser(self):
        """
        Test GET method to render update_review.html template as superuser
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test_superuser', password='password')
        response = self.client.get(('/profile/order_history/'
                                    f'{order.order_number}/'
                                    f'{orderreview.slug}/update/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_history/update_review.html')

    def test_post_updateorderreview_without_login(self):
        """
        Test POST method to submit a form to update record without login
        """
        order = self.order
        orderreview = self.orderreview
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/update/'), {
            'order_status': 2,
            'review': 'Test update review content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profile/' +
                             f'order_history/{order.order_number}/'
                             f'{orderreview.slug}/update/')

    def test_post_updateorderreview_valid_user(self):
        """
        Test POST method to submit a form to update record as valid user
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/update/'), {
            'order_status': 2,
            'review': 'Test update review content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/profile/order_history/' +
                              f'{order.order_number}/{orderreview.slug}/'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Review successfully updated.')

    def test_post_updateorderreview_invalid_user(self):
        """
        Test POST method to submit a form to update record as invalid user
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test2', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/update/'), {
            'order_status': 2,
            'review': 'Test update review content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("Access Denied.<br/>"
                                   "Only order owner and admin "
                                   "can do this action."))

    def test_post_updateorderreview_superuser(self):
        """
        Test POST method to submit a form to update record as superuser
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test_superuser', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/update/'), {
            'order_status': 2,
            'review': 'Test update review content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/profile/order_history/' +
                              f'{order.order_number}/{orderreview.slug}/'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Review successfully updated.')

    def test_post_updateorderreview_invalid_input(self):
        """
        Test POST method to submit invalid form input to update record
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/update/'), {
            'order_status': 6,
            'review': 'Test update review content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             ('/profile/order_history/' +
                              f'{order.order_number}/{orderreview.slug}/'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe('Invalid Input.<br/>'
                                   'Please check your input and try again!'))

    def test_post_deleteorderreview_without_login(self):
        """
        Test POST method to delete a record from data model without login
        """
        order = self.order
        orderreview = self.orderreview
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/delete/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             '/accounts/login/?next=/profile/' +
                             f'order_history/{order.order_number}/'
                             f'{orderreview.slug}/delete/')

    def test_post_deleteorderreview_valid_user(self):
        """
        Test POST method to delete a record from data model as valid user
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/delete/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Your order review is successfully removed.')

    def test_post_deleteorderreview__invalid_user(self):
        """
        Test POST method to delete a record from data model as invalid user
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test2', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/delete/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         mark_safe("Access Denied.<br/>"
                                   "Only order owner and admin "
                                   "can do this action."))

    def test_post_deleteorderreview_superuser(self):
        """
        Test POST method to delete a record from data model as superuser
        """
        order = self.order
        orderreview = self.orderreview
        self.client.login(username='test_superuser', password='password')
        response = self.client.post(('/profile/order_history/'
                                     f'{order.order_number}/'
                                     f'{orderreview.slug}/delete/'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Your order review is successfully removed.')
