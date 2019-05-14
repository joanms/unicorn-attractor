from django.contrib import admin
from .models import Feature, FeatureComment, FeatureUpvote

admin.site.register(Feature)
admin.site.register(FeatureComment)
admin.site.register(FeatureUpvote)