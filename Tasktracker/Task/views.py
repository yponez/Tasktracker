from datetime import datetime
from django.utils import timezone

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .Serializer import DeveloperSerializer, TaskSerializer, StartTimeSerializer
from .models import Developer,Task


class DeveloperCreateView(generics.CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class DeveloperUpdateView(generics.UpdateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class StarTimeView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.start_time:
            return Response("Отсчет времени уже начат.")

        task.start_time = timezone.now()
        task.save()

        return Response({"Отсчет времени начат.", task.start_time}, status = 200)


