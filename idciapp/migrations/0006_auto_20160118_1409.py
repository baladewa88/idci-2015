# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idciapp', '0005_delete_aacontactus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='papers',
            options={'managed': False},
        ),
    ]
