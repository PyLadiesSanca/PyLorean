# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151206_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='busy_weekday',
            field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')]),
        ),
    ]