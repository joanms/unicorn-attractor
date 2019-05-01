from django.conf.urls import url
from .views import report_bug, bug_detail, view_bugs

urlpatterns = [
    url(r'^view_bugs/$', view_bugs, name="view bugs"),
    url(r'^(?P<pk>\d+)/$', bug_detail, name="bug detail"),
    url(r'^report_bug/$', report_bug, name="report bug"),
]