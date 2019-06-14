from django.conf.urls import url, include
from .views import all_bugs, all_features, create_or_edit_bug, bug_detail, create_or_edit_feature, feature_detail

urlpatterns = [
    url(r'^bugs/', all_bugs, name='bugs'),
    url(r'^newbug/$', create_or_edit_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug'),

    url(r'^features/', all_features, name='features'),
    url(r'^newfeature/$', create_or_edit_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='bug_feature'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_feature, name='edit_feature')
]
