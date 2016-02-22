# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idciapp', '0007_auto_20160118_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='affiliasi',
            field=models.ForeignKey(db_column='affiliasi', default=0, to='idciapp.Affiliations'),
        ),
        migrations.AddField(
            model_name='papers',
            name='kodebuku',
            field=models.CharField(max_length=10, db_column='kodeBuku', default=0),
        ),
        migrations.AlterField(
            model_name='papers',
            name='crawldate',
            field=models.DateTimeField(db_column='crawlDate', default=0),
        ),
        migrations.AlterField(
            model_name='papers',
            name='id',
            field=models.CharField(serialize=False, primary_key=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='papers',
            name='ncites',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='papers',
            name='selfcites',
            field=models.IntegerField(db_column='selfCites'),
        ),
        migrations.AlterField(
            model_name='papers',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='papers',
            name='versiontime',
            field=models.DateTimeField(db_column='versionTime'),
        ),
    ]
