# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(related_name=b'orders', default=0, to='menu.Restaurant'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='food_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
