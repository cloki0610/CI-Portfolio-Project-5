""" Contact Data Model """
from django.db import models


class Contact(models.Model):
    """ Store contact details from customer """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=True, blank=True, default='')
    other_contact = models.CharField(max_length=50, null=True,
                                     blank=True, default='')
    message = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Data should order by date """
        ordering = ['-date']

    def __str__(self):
        return f"Message from {str(self.name)}"


class NewsLetter(models.Model):
    """ Store email for send news letter without login """
    email = models.EmailField(max_length=50)

    def __str__(self):
        return str(self.email)
