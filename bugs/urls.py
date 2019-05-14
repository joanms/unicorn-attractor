from django.conf.urls import url
from .views import report_bug, bug_details, list_bugs, upvote_bug, bug_comment

urlpatterns = [
    url(r'^list_bugs/$', list_bugs, name="list_bugs"),
    url(r'^(?P<pk>\d+)/$', bug_details, name="bug_details"),
    url(r'^report_bug/$', report_bug, name="report_bug"),
    # The code for upvoting is based on this: https://www.quora.com/How-do-I-create-a-vote-button-in-Django/answer/Lakshmi-Suvvada
    url(r'^upvote/(?P<bug_id>[0-9]+)/$', upvote_bug, name='upvote_bug'),
    url(r'^comment/(?P<pk>\d+)/$', bug_comment, name="bug_comment"),
]