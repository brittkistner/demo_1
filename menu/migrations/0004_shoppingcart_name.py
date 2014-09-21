# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20140921_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='name',
            field=models.CharField(default=b'shopping_cart', max_length=30),
            preserve_default=True,
        ),
    ]
