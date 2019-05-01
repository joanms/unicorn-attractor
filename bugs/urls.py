from django.conf.urls import url
from .views import report_bug, bug_detail, view_bugs

urlpatterns = [
    url(r'^report_bug/', report_bug, name="report bug"),
    url(r'^view_bugs/', view_bugs, name="view bugs"),
    url(r'^bug_detail/', bug_detail, name="bug detail"),
]