from django.contrib import admin
from .models import Bug, Comment, Upvote

admin.site.register(Bug)
admin.site.register(Comment)
admin.site.register(Upvote)