# Generated by Django 3.0.8 on 2020-09-15 05:11

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20200830_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 15, 12, 11, 4, 377081)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='img_main',
            field=models.ImageField(blank=True, upload_to='post_picture'),
        ),
        migrations.AlterField(
            model_name='post',
            name='vote',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
