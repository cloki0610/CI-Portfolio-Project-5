""" Report form model """
from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    """ Form model using Report data model """
    class Meta:
        """ Meta data """
        model = Report
        fields = ['name', 'problem_type',
                  'problem_description', 'contact_email']

    def __init__(self, *args, **kwargs):
        """
        Add style to each input item
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Tell us your Name',
            'problem_description': ('Please tell us some '
                                    'details of your product'),
            'contact_email': 'Contact E-mail (Optional)'
        }

        for field in self.fields:
            if field != 'problem_type':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} (Required)'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-success ' + \
                                                       'rounded-0 mb-2'
            self.fields[field].label = False
