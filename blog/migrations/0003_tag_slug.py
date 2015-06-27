# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150219_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 2, 19, 11, 51, 22, 577299), unique=True),
            preserve_default=False,
        ),
    ]
