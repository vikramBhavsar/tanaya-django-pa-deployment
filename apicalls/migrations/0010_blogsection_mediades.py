# Generated by Django 4.0.2 on 2022-04-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicalls', '0009_blog_ispublished_alter_artmediacontent_mediafile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsection',
            name='mediaDes',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
