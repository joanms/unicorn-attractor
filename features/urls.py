from django.conf.urls import url
from .views import request_feature, feature_details, list_features, upvote_feature, feature_comment

urlpatterns = [
    url(r'^list_features/$', list_features, name="list_features"),
    url(r'^(?P<pk>\d+)/$', feature_details, name="feature_details"),
    url(r'^report_feature/$', request_feature, name="request_feature"),
    # The code for upvoting is based on this: https://www.quora.com/How-do-I-create-a-vote-button-in-Django/answer/Lakshmi-Suvvada
    url(r'^upvote/(?P<feature_id>[0-9]+)/$', upvote_feature, name='upvote_feature'),
    url(r'^comment/(?P<pk>\d+)/$', feature_comment, name="feature_comment"),
]