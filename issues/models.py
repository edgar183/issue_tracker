from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .utils import ChoiceEnum


# Bug model 
class Bug(models.Model):
    model_name = 'Bug'
    title = models.CharField(max_length=125, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(User,related_name='bug_author', on_delete=models.CASCADE)
    class Statuses(ChoiceEnum):
        TODO = 'todo'
        DOING = 'doing'
        DONE = 'done'
    status = models.CharField(max_length=7, choices=Statuses.choices(), default='TODO', blank=True)

    def __str__(self):
        return self.title
        
# Feature model 
class Feature(models.Model):
    model_name = 'Feature'
    title = models.CharField(max_length=125, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_implemented = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(User,related_name='feature_author', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)
    class Statuses(ChoiceEnum):
        TODO = 'todo'
        DOING = 'doing'
        DONE = 'done'
    status = models.CharField(max_length=7, choices=Statuses.choices(), default='TODO', blank=True)

    def __str__(self):
        return self.title

class CommentBug(models.Model):     
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='bug_comment_author', on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, related_name='comment_bug', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class CommentFeature(models.Model):
       
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='feature_comment_author', on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, related_name='comment_feature', on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
