""" Report Data Model """
from django.db import models
from products.models import Product


TYPE = ((0, "Damaged"), (1, "Quality Problem"), (2, "Others"))


class Report(models.Model):
    """ Report of problem product from customer """
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="product_report")
    problem_type = models.IntegerField(choices=TYPE, default=0)
    problem_description = models.TextField(default='')
    report_on = models.DateTimeField(auto_now_add=True)
    contact_email = models.EmailField(max_length=50, blank=True, default='')
    checked = models.BooleanField(default=False)

    class Meta:
        """ Data should order by report date """
        ordering = ['-report_on']

    def __str__(self):
        return f"Report of {str(self.product)}"
