# Generated by Django 5.1.5 on 2025-02-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_remove_developer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='login',
        ),
        migrations.AlterField(
            model_name='developer',
            name='fullname',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
