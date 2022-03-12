""" OrderReview and Comment form model """
from django import forms
from .models import OrderReview, Comment


class OrderReviewForm(forms.ModelForm):
    """ Form model using OrderReview data model """
    class Meta:
        """ Meta data """
        model = OrderReview
        fields = ['order_status', 'review']

    def __init__(self, *args, **kwargs):
        """
        Add style to each input item
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'review':
                placeholder = 'Write down something about your order'
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-success ' + \
                                                       'rounded-0 mb-2'
            self.fields[field].label = False


class CommentForm(forms.ModelForm):
    """ Form model using Comment data model """

    class Meta:
        """ Meta data """
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        """
        Add style to each input item
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Comment Here'
            self.fields[field].widget.attrs['class'] = 'border-success ' + \
                                                       'rounded-0'
            self.fields[field].label = False
