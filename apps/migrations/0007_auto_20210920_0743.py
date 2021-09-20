# Generated by Django 3.2.7 on 2021-09-20 07:43

import apps.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_apps_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='publish_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='image',
            field=models.ImageField(default='', upload_to=apps.models.image_upload),
        ),
    ]