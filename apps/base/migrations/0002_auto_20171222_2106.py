# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-22 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloggerinfo',
            options={'verbose_name': '个人信息', 'verbose_name_plural': '个人信息列表'},
        ),
        migrations.AlterModelOptions(
            name='bloggermaster',
            options={'verbose_name': '技能信息', 'verbose_name_plural': '技能信息列表'},
        ),
        migrations.AlterModelOptions(
            name='bloggersocial',
            options={'verbose_name': '社交信息', 'verbose_name_plural': '社交信息列表'},
        ),
        migrations.AlterModelOptions(
            name='friendlink',
            options={'verbose_name': '友情链接', 'verbose_name_plural': '友情链接列表'},
        ),
        migrations.AlterModelOptions(
            name='siteinfo',
            options={'verbose_name': '网站信息', 'verbose_name_plural': '网站信息列表'},
        ),
        migrations.AlterField(
            model_name='bloggerinfo',
            name='background',
            field=models.ImageField(blank=True, help_text='背景图', null=True, upload_to='base/background/image/%y/%m', verbose_name='背景图'),
        ),
    ]
