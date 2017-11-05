# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('population', models.IntegerField()),
            ],
        ),
    ]