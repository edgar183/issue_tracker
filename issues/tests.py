from django.test import TestCase
from .models import Bug

# Create your tests here.
class BugTesting(TestCase):
    """
    Testing the Bug models
    """
    def test_str(self):
        test_bug_title= Bug(title='My First Bug')
        self.assertEqual(str(test_bug_title), 'My First Bug')