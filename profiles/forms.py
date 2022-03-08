""" UserProfile form model """
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Form model using UserProfile data model """
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=40)

    class Meta:
        """ Meta data """
        model = UserProfile
        exclude = ('user',)
        fields = [
                    'first_name', 'last_name', 'email', 'default_phone_number',
                    'default_postcode', 'default_town_or_city',
                    'default_street_address1', 'default_street_address2',
                    'default_county', 'default_country'
                 ]

    def save(self, *args, **kw):
        super(UserProfileForm, self).save(*args, **kw)
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.email = self.cleaned_data.get('email')
        self.instance.user.save()

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail address',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-success ' + \
                                                       'rounded-0 mb-2 ' + \
                                                       'profile-form-input'
            self.fields[field].label = False
