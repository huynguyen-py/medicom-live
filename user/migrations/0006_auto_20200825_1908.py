# Generated by Django 3.0.8 on 2020-08-25 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200813_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 19, 8, 37, 430475)),
        ),
    ]
