# Generated by Django 3.0.8 on 2020-10-12 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20201012_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 13, 52, 50, 882244)),
        ),
    ]
