# Generated by Django 3.0.8 on 2020-08-27 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200825_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 27, 20, 23, 19, 4426)),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
