""" Contact form model """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form model using Contact data model """
    class Meta:
        """ Meta data """
        model = Contact
        fields = ['name', 'email',
                  'other_contact', 'message']

    def __init__(self, *args, **kwargs):
        """
        Add style to each input item
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your Name',
            'email': 'Your E-mail',
            'other_contact': 'Other Contact method',
            'message': 'Your messages'
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} (Required)'
            else:
                placeholder = f'{placeholders[field]} (Optional)'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-success ' + \
                                                       'rounded-0 mb-2'
            self.fields[field].label = False
