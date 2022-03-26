""" Test forms in report application """
from django.test import TestCase
from .forms import ReportForm


class TestReportForms(TestCase):
    """ Test Report form model """

    def test_reportform_is_valid(self):
        """ Test report form model with valid input """
        form = ReportForm({
            'name': 'Test',
            'problem_type': 0,
            'problem_description': 'string for testing reportform',
            'contact_email': 'test@unittest.com',
        })
        self.assertTrue(form.is_valid())

    def test_name_is_required(self):
        """ Test with blank name input """
        form = ReportForm({
            'name': '',
            'problem_type': 0,
            'problem_description': 'string for testing reportform',
            'contact_email': 'test@unittest.com',
        })
        self.assertFalse(form.is_valid())

    def test_problem_type_is_required(self):
        """ Test with blank problem_type input """
        form = ReportForm({
            'name': 'Test',
            'problem_type': '',
            'problem_description': 'string for testing reportform',
            'contact_email': 'test@unittest.com',
        })
        self.assertFalse(form.is_valid())

    def test_problem_description_is_required(self):
        """ Test with blank problem_description input """
        form = ReportForm({
            'name': 'Test',
            'problem_type': 0,
            'problem_description': '',
            'contact_email': 'test@unittest.com',
        })
        self.assertFalse(form.is_valid())

    def test_contact_email_is_optional(self):
        """ Test with blank contact_email input """
        form = ReportForm({
            'name': 'Test',
            'problem_type': 0,
            'problem_description': 'string for testing reportform',
            'contact_email': '',
        })
        self.assertTrue(form.is_valid())
