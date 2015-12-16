# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idciapp', '0002_auto_20151216_0837'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='contactus',
            table='contact',
        ),
    ]
