# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 14:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0003_categories_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='users',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]
