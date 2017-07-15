# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-15 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='description_p',
            field=models.CharField(blank=True, default='N/A', max_length=1000),
        ),
        migrations.AlterField(
            model_name='education',
            name='skills',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='education',
            name='work',
            field=models.CharField(default='', max_length=100),
        ),
    ]
