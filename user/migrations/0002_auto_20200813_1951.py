# Generated by Django 3.0.8 on 2020-08-13 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 19, 51, 4, 359440)),
        ),
    ]
