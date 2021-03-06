""" Views of about """
from django.shortcuts import redirect, reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe
from .forms import ContactForm, NewsletterForm
from .models import Contact, NewsLetter


class About(generic.TemplateView):
    """ Return about template to show some information about our team """
    template_name = "about/about.html"


class ContactUs(generic.FormView):
    """ Return a form"""
    model = Contact
    template_name = 'about/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        # inherit form valid function, save the form and add message
        form.save()
        messages.success(self.request, 'Thank you for your support!')
        return super().form_valid(form)


class ContactList(LoginRequiredMixin, generic.ListView):
    """ Show a list of contact details """
    model = Contact

    def get(self, request, *args, **kwargs):
        """ GET method """
        # inherit the get method and deny user who is not superuser
        if not request.user.is_superuser:
            messages.error(request,
                           mark_safe('Request denied.<br/>'
                                     'Only admin can access.'))
            return redirect(reverse('home'))
        return super(ContactList, self).get(request, *args, **kwargs)


class NewsletterSubscribe(generic.FormView):
    """ Return a form to submit email """
    model = NewsLetter
    template_name = 'about/newsletter.html'
    form_class = NewsletterForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        # inherit form valid function, save the form and add message
        form.save()
        messages.success(self.request, 'Thank you for your subscribion!')
        return super().form_valid(form)
