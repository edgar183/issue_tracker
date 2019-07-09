from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bug, Feature, CommentBug, CommentFeature


class LoggedInTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='Customer', password='Pass1234')
        self.client.login(username='Customer', password='Pass1234')


class TestBugViews(LoggedInTestCase):

    def test_all_bug_page(self):
        page = self.client.get("/issues/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")

    def test_add_bug_page(self):
        page = self.client.get("/issues/new_bug/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugform.html")

    def test_edit_bug_page(self):
        user = User()
        user.save()
        bug = Bug(title="Test Bug Title",
                  description="Test Bug Description", author=user)
        bug.save()
        page = self.client.get("/issues/bug/{0}/edit_bug/".format(bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugform.html")

    def test_get_bug_detail_page(self):
        user = User()
        user.save()
        bug = Bug(title="Test Bug Title",
                      description="Test Bug Description", author=user)
        bug.save()
        page = self.client.get("/issues/bug/{0}/".format(bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugdetail.html")
    def test_edit_bug_page_for_item_that_does_not_exist(self):
        page = self.client.get("/issues/bug/1/edit_bug/")
        self.assertEqual(page.status_code, 404)

    def test_bug_detail_page_for_item_that_does_not_exist(self):
        page = self.client.get("/issues/bug/1/")
        self.assertEqual(page.status_code, 404)

    def test_add_commentBug_page(self):
        user = User()
        user.save()
        bug = Bug(title="Test Bug Title",
                      description="Test Bug Description", author=user)
        bug.save()
        page = self.client.get("/issues/bug/{0}/new_commet/".format(bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugcommentform.html")

    def test_edit_commentBug_page(self):
        user = User()
        user.save()
        bug = Bug(title="Test Bug Title",
                      description="Test Bug Description", author=user)
        bug.save()
        comment = CommentBug(comment="Test Bug Comment",
                          author=user, bug=bug)
        comment.save()
        page = self.client.get("/issues/bug/{0}/comment/{1}/edit/".format(bug.id, comment.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugcommentform.html")

    def test_edit_commentBug_page_for_item_that_does_not_exist(self):
        page = self.client.get("/issues/bug/1/coment/1/edit/")
        self.assertEqual(page.status_code, 404)

    

class TestFeatureViews(LoggedInTestCase):
    def test_get_feature_page(self):
        page = self.client.get("/issues/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")

    def test_add_feature_page(self):
        page = self.client.get("/issues/new_feature/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureform.html")

    def test_edit_bug_page(self):
        user = User()
        user.save()
        feature = Feature(title="Test Feature Title",
                          description="Test Feature Description", author=user, price=100.00)
        feature.save()
        page = self.client.get(
            "/issues/feature/{0}/edit_feature/".format(feature.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureform.html")

    def test_get_feature_detail_page(self):
        user = User()
        user.save()
        feature = Feature(title="Test Feature Title",
                      description="Test Feature Description", author=user, price=100.00)
        feature.save()
        page = self.client.get("/issues/feature/{0}/".format(feature.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featuredetail.html")
    
    def test_edit_feature_page_for_item_that_does_not_exist(self):
        page = self.client.get("/issues/feature/1/edit_bug/")
        self.assertEqual(page.status_code, 404)

    def test_bug_feature_page_for_item_that_does_not_exist(self):
        page = self.client.get("/issues/feature/1/")
        self.assertEqual(page.status_code, 404)

    def test_add_commentFeature_page(self):
        user = User()
        user.save()
        feature = Feature(title="Test Feature Title",
                      description="Test Feature Description", author=user, price=99.00)
        feature.save()
        page = self.client.get("/issues/feature/{0}/new_comment/".format(feature.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featurecommentform.html")

    def test_edit_commentFeature_page(self):
        user = User()
        user.save()
        feature = Feature(title="Test Feature Title",
                      description="Test Feature Description", author=user)
        feature.save()
        comment = CommentFeature(comment="Test Bug Comment",
                          author=user, feature=feature)
        comment.save()
        page = self.client.get("/issues/feature/{0}/comments/{1}/edit/".format(feature.id, comment.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featurecommentform.html")

    def test_edit_commentFeature_page_for_item_that_does_not_exist(self):
        page = self.client.get("/issues/feature/1/coments/1/edit/")
        self.assertEqual(page.status_code, 404)

