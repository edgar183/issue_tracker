from django.conf.urls import url, include
from .views import (
    all_bugs, 
    all_features, 
    create_or_edit_bug, 
    bug_detail, 
    create_or_edit_feature, 
    feature_detail, 
    create_or_edit_bug_comment, 
    upvote_bug, 
    upvote_feature, 
    create_or_edit_feature_comment,
    delete_bug,
    )


urlpatterns = [
    # bug urls
    url(r'^bugs/', all_bugs, name='bugs'),
    url(r'^newbug/$', create_or_edit_bug, name='new_bug'),
    url(r'^bug/(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^bug/(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug'),
    url(r'^bug/(?P<bug_pk>\d+)/new/$', create_or_edit_bug_comment, name='new_bug_comment'),
    url(r'bug/(?P<bug_pk>\d+)/(?P<pk>\d+)/edit/$', create_or_edit_bug_comment, name='edit_bug_comment'),
    url(r'bug/(?P<pk>\d+)/upvote/$', upvote_bug, name='upvote_bug'),
    url(r'bug/(?P<pk>\d+)/delete/$', delete_bug, name='delete_bug'),

    # feature urls
    url(r'^features/', all_features, name='features'),
    url(r'^newfeature/$', create_or_edit_feature, name='new_feature'),
    url(r'^feature/(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^feature/(?P<pk>\d+)/edit/$', create_or_edit_feature, name='edit_feature'),
    url(r'^feature/(?P<feature_pk>\d+)/new/$', create_or_edit_feature_comment, name='new_feature_comment'),
    url(r'feature/(?P<feature_pk>\d+)/(?P<pk>\d+)/edit/$', create_or_edit_feature_comment, name='edit_feature_comment'),
    url(r'^(?P<pk>\d+)/upvote/$', upvote_feature, name='upvote_feature'),
]
