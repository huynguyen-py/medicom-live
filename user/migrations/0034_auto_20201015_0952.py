# Generated by Django 3.0.8 on 2020-10-15 02:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_auto_20201015_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 15, 9, 52, 45, 616413)),
        ),
    ]
