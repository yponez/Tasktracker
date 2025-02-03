from django.shortcuts import render
from rest_framework import generics
from .Serializer import DeveloperSerializer
from .models import Developer


class DeveloperCreateView(generics.CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class DeveloperUpdateView(generics.UpdateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

