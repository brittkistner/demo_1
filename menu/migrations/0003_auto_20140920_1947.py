# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20140920_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='customer',
            field=models.ForeignKey(related_name=b'shopping_carts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='foods',
            field=models.ManyToManyField(related_name=b'shopping_carts', null=True, to=b'menu.Food'),
        ),
    ]
