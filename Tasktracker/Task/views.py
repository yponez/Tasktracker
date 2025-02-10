from datetime import datetime
from django.utils import timezone
from .DevActivity import  activityperiod,allactivityperiod,getsummactivityinterval,getactivityintervals
from rest_framework import generics, status
from rest_framework.response import Response
from .Serializer import DeveloperSerializer, TaskSerializer
from .models import Developer,Task
from rest_framework import generics

# добавить пользователя
class DeveloperCreateView(generics.CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

# изменить данные пользователя
class DeveloperUpdateView(generics.UpdateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

# начать отсчет времени задачи по ее id
class StarTimeView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.start_time:
            return Response("Отсчет времени уже начат.", status = status.HTTP_400_BAD_REQUEST)

        task.start_time = timezone.now()
        task.save()

        return Response({"Отсчет времени начат.", task.start_time}, status = 200)

# закончить отсчет времени задачи по ее id
class EndTimeView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.end_time:
            return Response("Отсчет времени уже закончен.", status = status.HTTP_400_BAD_REQUEST)
        elif task.start_time is None:
            return Response("Отсчет времени еще не начат.", status = status.HTTP_400_BAD_REQUEST)


        task.end_time = timezone.now()
        task.save()

        return Response({"Отсчет времени закончен.", task.end_time}, status = 200)

# показать все задачи разработчика и затраченное время в часах и минутах
class DevactivityPeriod(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        developer_id = self.kwargs.get('uuid')
        data = activityperiod(developer_id)
        return Response(data)

# показать трудозатраты всех разработчиков за период времени
class DevactivityPeriodAll(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):

        start_time_str = self.kwargs.get('start_time')
        end_time_str = self.kwargs.get('end_time')

        start_time = datetime.strptime(start_time_str, "%Y-%m-%d")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d")

        data = allactivityperiod(start_time, end_time)
        return Response(data)

# показать трудозатраты разработчика за период времени и суммарную активность
class DevmyactivityInterval(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get(self,request,*args,**kwargs):

        developer_id = self.kwargs.get('uuid')
        start_time_str = self.kwargs.get('start_time')
        end_time_str = self.kwargs.get('end_time')

        start_time = datetime.strptime(start_time_str, "%Y-%m-%d")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d")

        data = getsummactivityinterval(developer_id,start_time,end_time)
        return Response(data)

# показать все временные интервалы занятые активностью
class ActivityIntervals(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get(self,request,*args,**kwargs):

        start_time_str = self.kwargs.get('start_time')
        end_time_str = self.kwargs.get('end_time')

        start_time = datetime.strptime(start_time_str, "%Y-%m-%d")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d")

        data = getactivityintervals(start_time,end_time)
        return Response(data)

# удалить задачи разработчика по его id
class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def destroy(self, request, *args, **kwargs):
        developer_id = self.kwargs.get('developer_id')
        tasks = Task.objects.filter(developer_id = developer_id)
        if not tasks.exists():
            return Response("У разработчика нет задач")
        tasks.delete()
        return Response("Удалено")

# удалить всю информацию о разработчике по его id
class DeleteDeveloper(generics.DestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

    def destroy(self, request, *args, **kwargs):
        developer_id = self.kwargs.get('id')
        developers = Developer.objects.filter(id = developer_id)
        if not developers.exists():
            return Response("Такого разработчика нет")
        developers.delete()
        return Response("Удалено")