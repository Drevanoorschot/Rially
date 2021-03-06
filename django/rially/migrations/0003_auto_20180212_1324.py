# Generated by Django 2.0.2 on 2018-02-12 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('rially', '0002_auto_20180212_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submitted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('file', models.CharField(max_length=64)),
                ('received', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='TeamTelegramSession',
            fields=[
                ('telegram_chat_id', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='telegram_token',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teamtelegramsession',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rially.Team'),
        ),
        migrations.AddField(
            model_name='submitted',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rially.Team'),
        ),
    ]
