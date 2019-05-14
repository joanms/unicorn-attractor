from django.conf.urls import url
from .views import report_feature, feature_detail, view_features, upvote_feature, feature_comment

urlpatterns = [
    url(r'^view_features/$', view_features, name="view features"),
    url(r'^(?P<pk>\d+)/$', feature_detail, name="feature detail"),
    url(r'^report_feature/$', report_feature, name="report feature"),
    # The code for upvoting is based on this: https://www.quora.com/How-do-I-create-a-vote-button-in-Django/answer/Lakshmi-Suvvada
    url(r'^upvote/(?P<feature_id>[0-9]+)/$', upvote_feature, name='upvote feature'),
    url(r'^comment/(?P<pk>\d+)/$', feature_comment, name="comment on a feature"),
]