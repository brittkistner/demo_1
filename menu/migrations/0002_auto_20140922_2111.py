# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='yelp_id',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(related_name=b'orders', default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
