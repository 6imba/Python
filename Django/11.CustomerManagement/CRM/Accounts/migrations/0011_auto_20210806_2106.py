# Generated by Django 3.2.5 on 2021-08-06 15:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounts', '0010_auto_20210806_1241'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='profile',
        ),
    ]