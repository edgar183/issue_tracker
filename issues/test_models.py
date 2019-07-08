from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bug

# Create your tests here.


class TestBugModel(TestCase):
    """
    Testing the Bug models
    """

    def test_create_bug(self):
        user = User()
        #user.save()
        bug = Bug(title="Test bug title",
                  description="Test bug description", author=user, tag="Test")
        #bug.save()
        self.assertEqual(bug.title, "Test bug title")
        self.assertEqual(bug.description, "Test bug description")
        self.assertEqual(bug.author, user)
        self.assertFalse(bug.is_resolved)
        self.assertEqual(bug.status, "TODO")
        self.assertEqual(bug.tag, "Test")
        self.assertEqual(bug.upvotes, 0)

    def test_bug_as_a_string(self):
        bug = Bug(title="Test Title")
        self.assertEqual("Test Title", str(bug))
