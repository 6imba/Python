# Generated by Django 3.2 on 2021-05-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('desciption', models.CharField(max_length=300)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]