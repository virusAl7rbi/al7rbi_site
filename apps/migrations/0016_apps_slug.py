# Generated by Django 3.2.7 on 2021-09-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0015_auto_20210920_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
