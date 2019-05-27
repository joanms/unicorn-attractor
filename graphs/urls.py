from django.conf.urls import url
from .views import graphs

urlpatterns = [
    url(r'^graphs/$', graphs, name="graphs"),
]