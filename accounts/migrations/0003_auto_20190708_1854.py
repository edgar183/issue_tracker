# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-08 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='avatar/'),
        ),
    ]