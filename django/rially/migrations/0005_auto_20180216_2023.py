# Generated by Django 2.0.2 on 2018-02-16 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rially', '0004_auto_20180216_2018'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locationsolve',
            unique_together={('location', 'team')},
        ),
        migrations.AlterUniqueTogether(
            name='locationtasksolve',
            unique_together={('task', 'team')},
        ),
        migrations.AlterUniqueTogether(
            name='picturesolve',
            unique_together={('picture', 'team')},
        ),
        migrations.AlterUniqueTogether(
            name='tasksolve',
            unique_together={('task', 'team')},
        ),
    ]
