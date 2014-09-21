# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20140920_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='restaurant',
            field=models.ForeignKey(related_name=b'shopping_carts', to='menu.Restaurant'),
        ),
    ]
