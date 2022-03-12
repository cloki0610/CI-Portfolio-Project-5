""" Order Review and Comment Data Model """
from django.db import models
from django.utils.text import slugify
from profiles.models import UserProfile
from checkout.models import Order


STATUS = ((0, "Ordered"), (1, "Delivering"), (2, "Recieved"),
          (3, "Unknown"), (4, "Canceled"))


class OrderReview(models.Model):
    """ A Review for member's previous order """
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    customer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name="order_reviews")
    order_status = models.IntegerField(choices=STATUS, default=0)
    review = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    class Meta:
        """ Order by date from latest to oldest """
        ordering = ['-date']

    def __str__(self):
        return str(f"{str(self.customer)}-{str(self.order)}")

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the slug if it is empty.
        """
        if not self.slug:
            self.slug = slugify(str(self))
        super().save(*args, **kwargs)


class Comment(models.Model):
    """ The Comment in customer review """
    order_review = models.ForeignKey(OrderReview, on_delete=models.CASCADE,
                                     related_name="comments")
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, blank=True,
                             related_name="review_comments")
    comment = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ The data should order by created date """
        ordering = ['date']

    def __str__(self):
        return f"{str(self.user)} - Reply on {self.order_review}"
