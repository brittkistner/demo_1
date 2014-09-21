# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20140920_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='foods',
            field=models.ManyToManyField(related_name=b'shopping_carts', null=True, to=b'menu.Food', blank=True),
        ),
    ]
