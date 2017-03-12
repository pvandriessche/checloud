# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuideWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guideWord_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PhaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('phaItem_text', models.CharField(max_length=200)),
                ('guideWord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pha.GuideWord')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pha.Node')),
            ],
        ),
    ]
