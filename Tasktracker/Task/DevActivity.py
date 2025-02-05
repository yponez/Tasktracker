from django.db.models.expressions import result
from django.utils import timezone
from datetime import timedelta
from .models import Developer,Task

def activityPeriod(developer_id):

    result =[]
    tasks = Task.objects.filter(
        developer_id = developer_id,
    )
    for task in tasks:
        if task.start_time and task.end_time:
            seconds = task.activity
            minutes = seconds//60
            hours = minutes//60
            time_spend = f"hours:{hours}, minutes:{minutes}"

            result.append({
                'description': task.description,
                'time_spend' :time_spend,
                'total_seconds': seconds
            })
    result.sort(key = lambda x: x['total_seconds'],reverse= True )

    for item in result:
        item.pop('total_seconds')

    return result


