# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pha', '0004_auto_20170306_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hierachy',
            name='type',
        ),
        migrations.AddField(
            model_name='hierachy',
            name='depth',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hierachy',
            name='name',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hierachy',
            name='numchild',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hierachy',
            name='path',
            field=models.CharField(default='test', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
