# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-19 00:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='captain',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
    ]
