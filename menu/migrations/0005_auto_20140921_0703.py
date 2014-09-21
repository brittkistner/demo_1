# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_shoppingcart_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodandcount',
            name='food',
        ),
        migrations.DeleteModel(
            name='FoodAndCount',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='foods',
            field=models.ManyToManyField(related_name=b'orders', to='menu.Food'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='foods',
            field=models.ManyToManyField(related_name=b'shopping_carts', null=True, to='menu.Food', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='food_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='food_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
