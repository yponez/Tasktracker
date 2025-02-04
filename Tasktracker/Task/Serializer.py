from rest_framework import serializers
from .models import Developer,Task


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['id', 'fullname']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','developer_id','description','start_time','end_time']



