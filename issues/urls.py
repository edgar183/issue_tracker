from django.conf.urls import url, include
from .views import all_bugs, all_features

urlpatterns = [
    url(r'^bugs/', all_bugs, name='bugs'),
    url(r'^features/', all_features, name='features')
    
]