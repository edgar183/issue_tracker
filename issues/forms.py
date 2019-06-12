from django import forms
from .models import Feature, Bug, CommentBug, CommentFeature

class BugForm(forms.Form):
    class Meta:
        model = Bug
        fields = ('title', 'description', 'tag')
        
class FeatureForm(forms.Form):
    class Meta:
        model = Feature
        fields = ('title', 'description', 'tag')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentBug
        fields = ('comment',)