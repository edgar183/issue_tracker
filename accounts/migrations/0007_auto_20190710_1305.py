# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-10 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190710_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='avatar'),
        ),
    ]
