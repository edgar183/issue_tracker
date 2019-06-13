from django.conf.urls import url, include
from .views import all_bugs, all_features, create_or_edit_bug

urlpatterns = [
    url(r'^bugs/', all_bugs, name='bugs'),
    url(r'^features/', all_features, name='features'),
    url(r'^newbug/$', create_or_edit_bug, name='new_bug'),
]