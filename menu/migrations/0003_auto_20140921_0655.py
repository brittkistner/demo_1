# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20140921_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='food_quantity',
            field=models.ManyToManyField(related_name=b'shopping_cart', to=b'menu.FoodAndCount', blank=True),
        ),
    ]
