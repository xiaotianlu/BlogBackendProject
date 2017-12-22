# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-22 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_albuminfo_post_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albuminfo',
            options={'verbose_name': '图集', 'verbose_name_plural': '图集列表'},
        ),
        migrations.AlterModelOptions(
            name='albumphoto',
            options={'verbose_name': '图集图片', 'verbose_name_plural': '图集图片列表'},
        ),
        migrations.RemoveField(
            model_name='albuminfo',
            name='post_type',
        ),
    ]
