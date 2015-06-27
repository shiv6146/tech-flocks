# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 2, 52, 22, 790354)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='hits',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
