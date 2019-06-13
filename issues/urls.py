from django.conf.urls import url, include
from .views import all_bugs, all_features, bug_form

urlpatterns = [
    url(r'^bugs/', all_bugs, name='bugs'),
    url(r'^features/', all_features, name='features'),
    url(r'^newbug/$', bug_form, name='new_bug'),
]