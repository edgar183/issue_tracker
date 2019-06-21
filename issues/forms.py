from django import forms
from .models import Feature, Bug, CommentBug, CommentFeature

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'description', 'tag', 'is_resolved', 'status')
        
class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'description', 'tag', 'is_implemented', 'status')
        
class CommentBugForm(forms.ModelForm):
    class Meta:
        model = CommentBug
        fields = ('comment',)

class CommentFeatureForm(forms.ModelForm):
    class Meta:
        model = CommentFeature
        fields = ('comment',)