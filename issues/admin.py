from django.contrib import admin
from .models import Bug, Feature, Comment

# Register your models here.
admin.site.register(Bug)
admin.site.register(Feature)
admin.site.register(Comment)