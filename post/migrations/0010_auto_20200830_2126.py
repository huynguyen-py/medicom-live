# Generated by Django 3.0.8 on 2020-08-30 14:26

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20200827_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, default='Body post', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 30, 21, 26, 0, 244728)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply_comment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='post.Comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 30, 21, 26, 0, 243731)),
        ),
    ]
