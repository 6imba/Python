# Generated by Django 3.2.5 on 2021-09-29 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0011_auto_20210806_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status1',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
