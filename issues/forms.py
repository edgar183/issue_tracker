from django import forms
from .models import Feature, Bug, CommentBug, CommentFeature

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'description', 'tag')
        
class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'description', 'tag')
        
class CommentBugForm(forms.ModelForm):
    class Meta:
        model = CommentBug
        fields = ('comment',)

class CommentFeatureForm(forms.ModelForm):
    class Meta:
        model = CommentFeature
        fields = ('comment',)