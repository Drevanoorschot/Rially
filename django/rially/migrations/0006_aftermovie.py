# Generated by Django 2.0.2 on 2018-02-16 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rially', '0005_auto_20180216_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aftermovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.CharField(max_length=50)),
            ],
        ),
    ]
