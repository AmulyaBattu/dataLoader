# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-01 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dl', '0004_remove_userdata_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='userCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.IntegerField()),
                ('itemList', models.CharField(max_length=100)),
                ('itemPrice', models.CharField(max_length=100)),
                ('totalCost', models.FloatField(max_length=500)),
            ],
        ),
    ]
