# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-13 06:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170512_0957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Добавить пост блога', 'verbose_name_plural': '2. Посты блога'},
        ),
        migrations.AlterUniqueTogether(
            name='readpost',
            unique_together=set([('user', 'post')]),
        ),
        migrations.AlterIndexTogether(
            name='readpost',
            index_together=set([('user', 'post')]),
        ),
    ]
