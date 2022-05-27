# Generated by Django 4.0.2 on 2022-04-23 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apicalls', '0007_rename_sectionid_artmediacontent_projectid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogName', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='BlogSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionType', models.CharField(default='T', max_length=5)),
                ('sectionText', models.TextField(blank=True)),
                ('mediaURL', models.ImageField(blank=True, upload_to='blogs/%H_%M_%S_%f')),
                ('videoURL', models.TextField(blank=True, default='')),
                ('blogID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_sections', to='apicalls.blog')),
            ],
        ),
        migrations.CreateModel(
            name='MediaGroupSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediaURL', models.ImageField(blank=True, upload_to='blogs/%H_%M_%S_%f')),
                ('BlogSectionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_group_section', to='apicalls.blogsection')),
            ],
        ),
    ]