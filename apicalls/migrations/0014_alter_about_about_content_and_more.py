# Generated by Django 4.0.2 on 2022-05-01 05:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apicalls', '0013_about_alter_blogsection_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_content',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='blogsection',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 5, 49, 54, 829404, tzinfo=utc)),
        ),
    ]
