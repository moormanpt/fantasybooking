# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-13 03:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180513_0259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
        migrations.RenameField(
            model_name='match',
            old_name='match_name',
            new_name='name',
        ),
    ]
