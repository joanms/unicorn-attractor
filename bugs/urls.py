from django.conf.urls import url
from .views import report_bug, bug_detail, view_bugs, upvote, comment

urlpatterns = [
    url(r'^view_bugs/$', view_bugs, name="view bugs"),
    url(r'^(?P<pk>\d+)/$', bug_detail, name="bug detail"),
    url(r'^report_bug/$', report_bug, name="report bug"),
    url(r'^view_bugs/upvote/(?P<bug_id>[0-9]+)/$', upvote, name='upvote'),
    url(r'^comment/(?P<bug_id>[0-9]+)/$', comment, name="comment on a bug"),
]