# Generated by Django 3.0.3 on 2020-06-28 13:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Create_Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 13, 54, 23, 297361, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='Create_Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 13, 54, 23, 297361, tzinfo=utc)),
        ),
    ]
