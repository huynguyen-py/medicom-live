# Generated by Django 3.0.8 on 2020-10-12 05:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20201011_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 12, 1, 57, 802498)),
        ),
    ]
