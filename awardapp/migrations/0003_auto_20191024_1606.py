# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-24 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0002_auto_20191024_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
