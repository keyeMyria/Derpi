# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0009_auto_20170216_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensors',
            name='sensor_types',
            field=models.CharField(choices=[('SW', 'On off switch'), ('OU', 'Sensor output'), ('SL', 'Data slider')], default='SW', max_length=2),
        ),
    ]
