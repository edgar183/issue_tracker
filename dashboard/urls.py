from django.conf.urls import url, include
from .views import chart

urlpatterns = [
  url(r'^dashboard/$', chart, name='dashboard' )
]