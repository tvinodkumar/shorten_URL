# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField()),
                ('designation', models.CharField(max_length=100)),
                ('visitDate', models.DateField()),
                ('purposeOfVisit', models.CharField(max_length=100)),
                ('visitDuration', models.IntegerField(max_length=3)),
                ('comments', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('phone_no', models.IntegerField()),
                ('driving_lic_no', models.IntegerField(max_length=20)),
                ('company', models.CharField(max_length=50)),
                ('comingFrom', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(to='visitor.Employee')),
            ],
        ),
    ]
