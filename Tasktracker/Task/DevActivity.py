from django.utils import timezone
from datetime import  datetime
from .models import Task

def activityperiod(developer_id):

    result =[]
    tasks = Task.objects.filter(
        developer_id = developer_id,
    )
    for task in tasks:
        if task.start_time and task.end_time:
            seconds = task.activity
            minutes = (seconds % 3600) //60
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

def allactivityperiod(start_time,end_time):

    result = {
        "count": 0,
        "users": []
    }

    if isinstance(start_time, datetime) and timezone.is_naive(start_time):
        start_time = timezone.make_aware(start_time)

    if isinstance(end_time, datetime) and timezone.is_naive(end_time):
        end_time = timezone.make_aware(end_time)


    tasks = Task.objects.filter(
        start_time__gte = start_time,
        end_time__lte = end_time
    )

    for task in tasks:
        if task.start_time and task.end_time:
            user_id = task.developer.id
            fullname = task.developer.fullname
            hours = task.activity // 3600
            periodtasks = []

            periodtasks.append({"id":task.id,"description":task.description,"activity":hours})
            result["users"].append({
                "id":user_id,
                "fullname":fullname,
                "TASKS_USER": periodtasks,
            })
            result["count"] += 1

    return result

def getsummactivityinterval(developer_id,start_time,end_time):
    intervals = []
    summactivity = {
        "hours": 0,
        "minutes": 0
    }

    if isinstance(start_time, datetime) and timezone.is_naive(start_time):
        start_time = timezone.make_aware(start_time)

    if isinstance(end_time, datetime) and timezone.is_naive(end_time):
        end_time = timezone.make_aware(end_time)

    tasks = Task.objects.filter(
        developer_id = developer_id,
        start_time__gte=start_time,
        end_time__lte=end_time
    )

    for task in tasks:
        if task.start_time and task.end_time:
            seconds = task.activity
            minutes = (seconds %3600) // 60
            hours = seconds //3600

            summactivity["hours"] += hours
            summactivity["minutes"] += minutes

            interval_str = f"hours:{hours}, minutes:{minutes}"

            intervals.append(f"{interval_str} - {task.description}")

    intervals.append(f"Sum activity: "
                     f"hours:{summactivity['hours']} "
                     f"minutes:{summactivity['minutes']}")

    return intervals

def getactivityintervals(start_time,end_time):
    intervals = []

    if isinstance(start_time, datetime) and timezone.is_naive(start_time):
        start_time = timezone.make_aware(start_time)

    if isinstance(end_time, datetime) and timezone.is_naive(end_time):
        end_time = timezone.make_aware(end_time)

    tasks = Task.objects.filter(
        start_time__gte=start_time,
        end_time__lte=end_time
    )

    for task in tasks:
        if task.start_time and task.end_time:
            seconds = task.activity
            minutes = (seconds %3600) // 60
            hours = seconds //3600

            interval_date = f"start:{task.start_time} end:{task.end_time}"
            interval_str = f"hours:{hours}, minutes:{minutes}"

            intervals.append(f"({interval_date}) - ({interval_str}) - ({task.description})")

    return intervals