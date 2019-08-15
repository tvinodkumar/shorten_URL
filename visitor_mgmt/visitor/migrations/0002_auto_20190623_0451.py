# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='phone_no',
            field=models.IntegerField(unique=True),
        ),
    ]
