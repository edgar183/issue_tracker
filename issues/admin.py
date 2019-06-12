from django.contrib import admin
from .models import Bug, Feature, CommentBug, CommentFeature

# Register your models here.
admin.site.register(Bug)
admin.site.register(Feature)
admin.site.register(CommentBug)
admin.site.register(CommentFeature)