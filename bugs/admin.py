from django.contrib import admin
from .models import Bug, BugComment, BugUpvote

admin.site.register(Bug)
admin.site.register(BugComment)
admin.site.register(BugUpvote)