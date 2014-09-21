# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodandcount',
            name='food',
            field=models.ForeignKey(related_name=b'food_quantity', blank=True, to='menu.Food', null=True),
        ),
    ]
