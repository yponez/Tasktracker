from django.urls import re_path
from .views import DeveloperUpdateView,StarTimeView

urlpatterns = [
    re_path(r'^updateDev/(?P<pk>[0-9a-f]{32})/$', DeveloperUpdateView.as_view()),
    re_path(r'^startTime/(?P<pk>[0-9a-f]{32})/$', StarTimeView.as_view()),
]