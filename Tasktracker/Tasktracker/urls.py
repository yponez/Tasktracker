"""
URL configuration for Tasktracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.contrib import admin
from django.urls import path, re_path, include
from Task.views import (DeveloperCreateView, DevactivityPeriod, DevactivityPeriodAll,
                        DevmyactivityInterval, ActivityIntervals, DeleteTask,
                        DeleteDeveloper)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Task.urls')),
    path('createDev/',DeveloperCreateView.as_view(),
         name = 'createDev'),
    path('devActivityPeriod/<uuid:uuid>/',DevactivityPeriod.as_view(),
         name = 'devActivityPeriod'),
    path('devPeriodAll/<str:start_time>/<str:end_time>/',DevactivityPeriodAll.as_view(),
         name = 'devPeriodAll'),
    path('devMyActivity/<str:start_time>/<str:end_time>/<uuid:uuid>/',DevmyactivityInterval.as_view(),
         name = 'devMyActivity'),
    path('activityIntervals/<str:start_time>/<str:end_time>/',ActivityIntervals.as_view(),
         name = 'activityIntervals'),
    path('DeleteTaskData/<uuid:developer_id>/',DeleteTask.as_view(),
         name = 'DeleteTaskData'),
    path('DeleteDeveloper/<uuid:id>/',DeleteDeveloper.as_view(),
         name = 'DeleteDeveloper'),
]
