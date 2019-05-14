from django.conf.urls import url
from .views import report_bug, bug_detail, view_bugs, upvote_bug, bug_comment

urlpatterns = [
    url(r'^view_bugs/$', view_bugs, name="view bugs"),
    url(r'^(?P<pk>\d+)/$', bug_detail, name="bug detail"),
    url(r'^report_bug/$', report_bug, name="report bug"),
    # The code for upvoting is based on this: https://www.quora.com/How-do-I-create-a-vote-button-in-Django/answer/Lakshmi-Suvvada
    url(r'^upvote/(?P<bug_id>[0-9]+)/$', upvote_bug, name='upvote bug'),
    url(r'^comment/(?P<pk>\d+)/$', bug_comment, name="comment on a bug"),
]