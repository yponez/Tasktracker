import os
from http.client import responses

import django
from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APITestCase
from django.urls import reverse
from win32comext.shell.demos.servers.folder_view import tasks

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tasktracker.settings')
django.setup()
from Task.models import Developer
from Task.models import Task



class TestTask(APITestCase):

    def setUp(self):
        self.developer = Developer.objects.create(
            id = '689fb46c-6190-4f2b-aaa6-88d882496410',
            fullname = 'PetrTest'
        )
        self.task1 = Task.objects.create(
            id = 'cc37a882-dd31-46ed-826e-4efafb21a3cd',
            description = 'Create API',
            start_time = timezone.now(),
            end_time = timezone.now(),
            developer_id = '689fb46c-6190-4f2b-aaa6-88d882496410'
        )
        self.task2 = Task.objects.create(
            id='d38cb5d6f7e04822b13bd6fdd9f544c5',
            description= 'Refactoring',
            start_time=None,
            end_time=None,
            developer_id='689fb46c-6190-4f2b-aaa6-88d882496410'
        )
        self.task3 = Task.objects.create(
            id='ceb498ce2ce94d93bd4a8043e2835342',
            description='Create method',
            start_time=timezone.now(),
            end_time=None,
            developer_id='689fb46c-6190-4f2b-aaa6-88d882496410'
        )

    def test_get_ActivityPeriod(self):
        url = reverse('devActivityPeriod',kwargs = {'uuid':self.developer.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data[0]['description'],'Create API')
        self.assertEqual(response.data[0]['time_spend'], 'hours:0, minutes:0')

    def test_post_StartTime200(self):
        url = reverse('startTime', kwargs = {'pk':self.task2.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code,200)

    def test_post_StartTime400(self):
        url = reverse('startTime', kwargs={'pk': self.task3.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)

    def test_post_endTime400(self):
        url = reverse('endTime', kwargs = {'pk':self.task2.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code,400)

    def test_get_devPeriodAll(self):
        url = reverse('devPeriodAll',
                      kwargs ={'start_time': '2025-02-01','end_time': '2025-02-10'})
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['count'],1)

    def test_get_devMyActivity(self):
        url = reverse('devMyActivity',
                      kwargs = {'start_time': '2025-02-01','end_time': '2025-02-10','uuid':self.developer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_get_activityIntervals(self):
        url = reverse('activityIntervals',
                      kwargs={'start_time': '2025-02-01','end_time': '2025-02-10'})
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)\

    def test_deleteTask(self):
        url = reverse('DeleteTaskData',kwargs = {'developer_id':'689fb46c-6190-4f2b-aaa6-88d882496410'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code,200)



class TestDeveloper(APITestCase):
    def setUp(self):
        self.developer = Developer.objects.create(
            id = '689fb46c-6190-4f2b-aaa6-88d882496410',
            fullname = 'PetrTest'
        )
        self.task1 = Task.objects.create(
            id = 'cc37a882-dd31-46ed-826e-4efafb21a3cd',
            description = 'Create API',
            start_time = timezone.now(),
            end_time = timezone.now(),
            developer_id = '689fb46c-6190-4f2b-aaa6-88d882496410'
        )

    def test_deleteDeveloper(self):
        url = reverse('DeleteDeveloper',kwargs = {'id':'689fb46c-6190-4f2b-aaa6-88d882496410'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code,200)

    def test_createDeveloper(self):
        url = reverse('createDev')
        response = self.client.post(url,{'fullname':'Test'})
        self.assertEqual(response.status_code,201)


