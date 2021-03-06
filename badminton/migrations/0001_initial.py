# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('club', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('about', models.TextField()),
                ('member_since', models.DateField(default=django.utils.timezone.now)),
                ('nfc_id', models.IntegerField()),
            ],
        ),
    ]
