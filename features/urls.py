from django.conf.urls import url
from .views import request_feature, feature_details, list_features, feature_comment

urlpatterns = [
    url(r'^list_features/$', list_features, name="list_features"),
    url(r'^(?P<pk>\d+)/$', feature_details, name="feature_details"),
    url(r'^request_feature/$', request_feature, name="request_feature"),
    url(r'^comment/(?P<pk>\d+)/$', feature_comment, name="feature_comment"),
]