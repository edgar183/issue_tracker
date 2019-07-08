from django.test import TestCase
from .forms import BugForm

# Create your tests here.


class BugFormTesting(TestCase):
    """
    Testing the Bug form
    """

    def test_bug_form_can_submit_with_required_fields(self):
        form = BugForm({'title': 'Test Title', 'description': 'Test Description'})
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_bug_form_correct_error_message_for_missing_required_fields(self):
        form = BugForm({'title': ''}, {'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        self.assertEqual(form.errors['description'], [u'This field is required.'])