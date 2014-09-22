# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderFoodQuantity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('food', models.ForeignKey(related_name=b'order_quantities', to='menu.Food')),
                ('order', models.ForeignKey(related_name=b'food_quantities', to='menu.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShoppingCartFoodQuantity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('food', models.ForeignKey(related_name=b'shopping_cart_quantities', to='menu.Food')),
                ('shopping_cart', models.ForeignKey(related_name=b'food_quantities', to='menu.ShoppingCart')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='order',
            name='food_quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='foods',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='food_quantity',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='foods',
        ),
    ]
