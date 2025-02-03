from django.urls import re_path
from .views import DeveloperUpdateView

urlpatterns = [
    re_path(r'^updateDev/(?P<pk>[0-9a-f]{32})/$', DeveloperUpdateView.as_view()),
]