# Generated by Django 2.0.2 on 2019-02-04 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rially', '0010_priorityqueue_queue'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Queue',
            new_name='PriorityQueueItem',
        ),
        migrations.RenameModel(
            old_name='PriorityQueue',
            new_name='QueueItem',
        ),
    ]
