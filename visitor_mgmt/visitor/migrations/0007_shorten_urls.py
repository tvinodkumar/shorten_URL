# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-15 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0006_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shorten_URLS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shorten_url', models.CharField(max_length=50)),
                ('url_name', models.CharField(max_length=250)),
            ],
        ),
    ]