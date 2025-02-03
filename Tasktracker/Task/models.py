from django.db import models
import uuid
from datetime import timedelta

class Developer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.fullname

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='tasks')
    description = models.CharField(max_length=255)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    @property
    def activity(self):
        if self.start_time and self.end_time:
            time_difference = self.end_time - self.start_time
            total_seconds = int(time_difference.total_seconds())
            return total_seconds// 3600
        return 0

    def __str__(self):
        return f"{self.description} by {self.developer.fullname}"