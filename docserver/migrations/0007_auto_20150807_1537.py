# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('docserver', '0006_auto_20150807_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='root_directory',
        ),
        migrations.RemoveField(
            model_name='document',
            name='collection',
        ),
    ]
