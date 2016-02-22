# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idciapp', '0008_auto_20160216_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='versiontime',
            field=models.DateTimeField(db_column='versionTime', default=0),
        ),
    ]
