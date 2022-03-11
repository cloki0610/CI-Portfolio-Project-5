""" Product form model """
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Form model using Product data model """
    class Meta:
        """ Meta data """
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Change category option to friendly name
        Add style to each input item
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        placeholders = {
            'sku': 'sku',
            'name': 'Product Name',
            'description': 'Description',
            'price': 'Product Price',
            'image_url': 'Image URL',
        }

        self.fields['category'].choices = friendly_names
        for field in self.fields:
            if (field == 'sku' or field == 'name' or field == 'description' or
                    field == 'price' or field == 'image_url'):
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} (Required)'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-success ' + \
                                                       'rounded-0 mb-2'
            self.fields[field].label = False
