# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-23 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(max_length=5)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('dob', models.DateField(max_length=10)),
            ],
        ),
    ]