# Generated by Django 2.0.2 on 2019-02-04 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rially', '0009_sitestate_show_scoreboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriorityQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sent', models.DateTimeField()),
                ('submitted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rially.Submitted')),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sent', models.DateTimeField()),
                ('submitted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rially.Submitted')),
            ],
        ),
    ]
