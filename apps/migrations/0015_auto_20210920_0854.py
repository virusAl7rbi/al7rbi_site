# Generated by Django 3.2.7 on 2021-09-20 08:54

import apps.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0014_auto_20210920_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='android_url',
            field=models.URLField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apps',
            name='description',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='apps',
            name='desk_lin_url',
            field=models.URLField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apps',
            name='desk_mac_url',
            field=models.URLField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apps',
            name='desk_win_url',
            field=models.URLField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apps',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=apps.models.image_upload),
        ),
        migrations.AlterField(
            model_name='apps',
            name='ios_url',
            field=models.URLField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='apps',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='web_url',
            field=models.URLField(blank=True, default='', max_length=100),
        ),
    ]
