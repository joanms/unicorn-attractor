from django.conf.urls import url
from .views import GraphView

urlpatterns = [
    url(r'^$', GraphView.as_view(), name="graphs"),
]