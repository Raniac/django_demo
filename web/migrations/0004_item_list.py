# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-08 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web.List'),
        ),
    ]
