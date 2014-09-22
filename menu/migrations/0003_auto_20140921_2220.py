# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20140921_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customers',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(related_name=b'orders', default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
