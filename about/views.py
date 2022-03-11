""" Views of about """
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


class About(generic.TemplateView):
    """ Return about template to show some information about our team """
    template_name = "about/about.html"


class ContactUs(generic.FormView):
    """ Return a form"""
    template_name = 'about/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        messages.success(self.request, 'Thank you for your support. ' +
                         'Our admin will contact you soon!')
        return super().form_valid(form)


class ContactList(LoginRequiredMixin, generic.ListView):
    """ Show a list of contact details """
    model = Contact
    paginate_by = 1
