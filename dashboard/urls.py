from django.conf.urls import url, include
from .views import (
  chart,
  get_bug_status_json, 
  get_feature_status_json,
  get_bug_upvotes_json, 
  get_feature_upvotes_json,
  get_issue_type_json
  )

urlpatterns = [
 url(r'^$', chart, name='dashboard' ),
  url(r'^get_bug_status_json/$', get_bug_status_json, name='get_bug_status_json'),
  url(r'^get_feature_status_json/$', get_feature_status_json, name='get_feature_status_json'),
  url(r'^get_bug_upvotes_json/$', get_bug_upvotes_json, name='get_bug_upvotes_json'),
  url(r'^get_feature_upvotes_json/$', get_feature_upvotes_json, name='get_feature_upvotes_json'),
  url(r'^get_issue_type_json/$', get_issue_type_json, name='get_issue_type_json'),
]