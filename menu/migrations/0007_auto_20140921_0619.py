# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20140920_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodAndCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('food', models.ForeignKey(related_name=b'food_quantity', to='menu.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='order',
            name='foods',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='foods',
        ),
        migrations.AlterField(
            model_name='order',
            name='food_quantity',
            field=models.ManyToManyField(related_name=b'orders', null=True, to=b'menu.FoodAndCount', blank=True),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='food_quantity',
            field=models.ManyToManyField(related_name=b'shopping_cart', null=True, to=b'menu.FoodAndCount', blank=True),
        ),
    ]
