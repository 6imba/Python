# Generated by Django 3.2.4 on 2021-07-04 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Custome_Blog_App', '0003_auto_20210704_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]