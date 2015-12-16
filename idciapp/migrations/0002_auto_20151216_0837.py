# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('idciapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acknowledgmentcontexts',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('context', models.TextField()),
            ],
            options={
                'db_table': 'acknowledgmentcontexts',
            },
        ),
        migrations.CreateModel(
            name='Acknowledgments',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('cluster', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('enttype', models.CharField(blank=True, null=True, max_length=20, db_column='entType')),
                ('acktype', models.CharField(blank=True, null=True, max_length=20, db_column='ackType')),
            ],
            options={
                'db_table': 'acknowledgments',
            },
        ),
        migrations.CreateModel(
            name='Affilauthmap',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('affiliations_id', models.BigIntegerField(blank=True, null=True)),
                ('authors_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'affilauthmap',
            },
        ),
        migrations.CreateModel(
            name='Affiliations',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(blank=True, null=True, max_length=1000)),
                ('address', models.CharField(blank=True, null=True, max_length=1000)),
                ('url', models.CharField(blank=True, null=True, max_length=500)),
                ('ncites', models.IntegerField(blank=True, null=True)),
                ('nauthors', models.IntegerField(blank=True, null=True)),
                ('ndocs', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'affiliations',
            },
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('cluster', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('affil', models.CharField(blank=True, null=True, max_length=255)),
                ('address', models.CharField(blank=True, null=True, max_length=255)),
                ('email', models.CharField(blank=True, null=True, max_length=100)),
                ('ord', models.IntegerField()),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Authorsaffil',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('authors_id', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, null=True, max_length=500)),
                ('address', models.CharField(blank=True, null=True, max_length=500)),
            ],
            options={
                'db_table': 'authorsaffil',
            },
        ),
        migrations.CreateModel(
            name='Cannames',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('canname', models.CharField(blank=True, null=True, max_length=100)),
                ('ndocs', models.IntegerField(blank=True, null=True)),
                ('ncites', models.IntegerField()),
                ('url', models.CharField(blank=True, null=True, max_length=250)),
                ('affil', models.CharField(blank=True, null=True, max_length=255)),
                ('address', models.CharField(blank=True, null=True, max_length=255)),
                ('email', models.CharField(blank=True, null=True, max_length=100)),
                ('hindex', models.IntegerField()),
            ],
            options={
                'db_table': 'cannames',
            },
        ),
        migrations.CreateModel(
            name='Checksum',
            fields=[
                ('sha1', models.CharField(serialize=False, primary_key=True, max_length=100)),
                ('filetype', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'checksum',
            },
        ),
        migrations.CreateModel(
            name='Citationcontexts',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('context', models.TextField()),
            ],
            options={
                'db_table': 'citationcontexts',
            },
        ),
        migrations.CreateModel(
            name='Citations',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('cluster', models.BigIntegerField(blank=True, null=True)),
                ('authors', models.TextField(blank=True, null=True)),
                ('title', models.CharField(blank=True, null=True, max_length=255)),
                ('venue', models.CharField(blank=True, null=True, max_length=255)),
                ('venuetype', models.CharField(blank=True, null=True, max_length=20, db_column='venueType')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('pages', models.CharField(blank=True, null=True, max_length=20)),
                ('editors', models.TextField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, null=True, max_length=100)),
                ('pubaddress', models.CharField(blank=True, null=True, max_length=100, db_column='pubAddress')),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('tech', models.CharField(blank=True, null=True, max_length=100)),
                ('raw', models.TextField(blank=True, null=True)),
                ('self', models.IntegerField()),
            ],
            options={
                'db_table': 'citations',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, null=True, max_length=50)),
                ('contact_email', models.CharField(blank=True, null=True, max_length=50)),
                ('contact_subject', models.CharField(blank=True, null=True, max_length=150)),
                ('contact_message', models.TextField()),
                ('contact_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Deletes',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('table_name', models.CharField(blank=True, null=True, max_length=50)),
                ('table_id', models.BigIntegerField(blank=True, null=True)),
                ('deleted_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'deletes',
            },
        ),
        migrations.CreateModel(
            name='Ealgorithms',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('proxyid', models.CharField(db_column='proxyID', max_length=100)),
                ('caption', models.CharField(blank=True, null=True, max_length=500)),
                ('synopsis', models.CharField(blank=True, null=True, max_length=2000)),
                ('reftext', models.CharField(blank=True, null=True, max_length=500)),
                ('pagenum', models.IntegerField(db_column='pageNum')),
                ('ncites', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ealgorithms',
            },
        ),
        migrations.CreateModel(
            name='Elinks',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'elinks',
            },
        ),
        migrations.CreateModel(
            name='Etables',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('proxyid', models.CharField(db_column='proxyID', max_length=100)),
                ('indocid', models.IntegerField(blank=True, null=True, db_column='inDocID')),
                ('caption', models.CharField(blank=True, null=True, max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
                ('footnote', models.CharField(blank=True, null=True, max_length=200, db_column='footNote')),
                ('reftext', models.CharField(blank=True, null=True, max_length=200, db_column='refText')),
                ('pagenum', models.IntegerField(db_column='pageNum')),
                ('updatetime', models.DateTimeField(db_column='updateTime')),
            ],
            options={
                'db_table': 'etables',
            },
        ),
        migrations.CreateModel(
            name='Hubmap',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'hubmap',
            },
        ),
        migrations.CreateModel(
            name='Huburls',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('url', models.CharField(unique=True, max_length=255)),
                ('lastcrawl', models.DateTimeField(db_column='lastCrawl')),
                ('repositoryid', models.CharField(blank=True, null=True, max_length=15, db_column='repositoryID')),
            ],
            options={
                'db_table': 'huburls',
            },
        ),
        migrations.CreateModel(
            name='Journals',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('venue_id', models.BigIntegerField()),
                ('volume', models.CharField(blank=True, null=True, max_length=20)),
                ('number', models.CharField(blank=True, null=True, max_length=20)),
                ('year', models.CharField(blank=True, null=True, max_length=4)),
            ],
            options={
                'db_table': 'journals',
            },
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('keyword', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'keywords',
            },
        ),
        migrations.CreateModel(
            name='Legacyidmap',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('legacyid', models.IntegerField()),
            ],
            options={
                'db_table': 'legacyidmap',
            },
        ),
        migrations.CreateModel(
            name='LinkTypes',
            fields=[
                ('label', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('baseurl', models.CharField(db_column='baseURL', max_length=255)),
            ],
            options={
                'db_table': 'link_types',
            },
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=100, default=1320, verbose_name='ID')),
                ('version', models.IntegerField()),
                ('cluster', models.BigIntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, null=True, verbose_name='Title', max_length=255)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('venue', models.CharField(blank=True, null=True, max_length=100)),
                ('venuetype', models.CharField(blank=True, null=True, max_length=20, db_column='venueType')),
                ('pages', models.CharField(blank=True, null=True, max_length=20)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, null=True, max_length=100)),
                ('pubaddress', models.CharField(blank=True, null=True, max_length=100, db_column='pubAddress')),
                ('tech', models.CharField(blank=True, null=True, max_length=100)),
                ('public', models.IntegerField()),
                ('ncites', models.IntegerField(verbose_name='Citations', default=0)),
                ('versionname', models.CharField(blank=True, null=True, max_length=20, db_column='versionName')),
                ('crawldate', models.DateTimeField(null=True, db_column='crawlDate', auto_now=True)),
                ('repositoryid', models.CharField(blank=True, null=True, max_length=15, db_column='repositoryID')),
                ('conversiontrace', models.CharField(blank=True, null=True, max_length=255, db_column='conversionTrace')),
                ('selfcites', models.IntegerField(db_column='selfCites', verbose_name='Self Citation', default=0)),
                ('versiontime', models.DateTimeField(null=True, db_column='versionTime', auto_now=True)),
            ],
            options={
                'db_table': 'papers',
            },
        ),
        migrations.CreateModel(
            name='Paperversions',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(blank=True, null=True, max_length=20)),
                ('version', models.IntegerField()),
                ('repositoryid', models.CharField(db_column='repositoryID', max_length=15)),
                ('path', models.CharField(max_length=255)),
                ('deprecated', models.IntegerField()),
                ('spam', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'paperversions',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('tag', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Textsources',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'textsources',
            },
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'urls',
            },
        ),
        migrations.CreateModel(
            name='Usercorrections',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('userid', models.CharField(max_length=100)),
                ('version', models.IntegerField()),
            ],
            options={
                'db_table': 'usercorrections',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.CharField(serialize=False, primary_key=True, max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('firstname', models.CharField(db_column='firstName', max_length=100)),
                ('middlename', models.CharField(blank=True, null=True, max_length=100, db_column='middleName')),
                ('lastname', models.CharField(db_column='lastName', max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('affil1', models.CharField(blank=True, null=True, max_length=255)),
                ('affil2', models.CharField(blank=True, null=True, max_length=255)),
                ('enabled', models.IntegerField()),
                ('country', models.CharField(blank=True, null=True, max_length=100)),
                ('province', models.CharField(blank=True, null=True, max_length=100)),
                ('webpage', models.CharField(blank=True, null=True, max_length=255, db_column='webPage')),
                ('internalid', models.BigIntegerField()),
                ('updated', models.DateTimeField()),
                ('appid', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Venuepapermap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('paperid', models.CharField(max_length=20)),
                ('venue_id', models.BigIntegerField()),
                ('venue_varname', models.CharField(blank=True, null=True, max_length=500)),
            ],
            options={
                'db_table': 'venuepapermap',
            },
        ),
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(blank=True, null=True, max_length=500)),
                ('url', models.CharField(blank=True, null=True, max_length=500)),
                ('editor', models.CharField(blank=True, null=True, max_length=500)),
                ('issn', models.CharField(blank=True, null=True, max_length=50)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('contact_info', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, null=True, max_length=20)),
                ('language', models.CharField(blank=True, null=True, max_length=20)),
                ('halflife_cited', models.FloatField(blank=True, null=True)),
                ('halflife_citing', models.FloatField(blank=True, null=True)),
                ('impact_factor', models.FloatField(blank=True, null=True)),
                ('immediciacy', models.FloatField(blank=True, null=True)),
                ('hindex', models.FloatField(blank=True, null=True)),
                ('selfcites', models.IntegerField(blank=True, null=True)),
                ('ndocs', models.IntegerField(blank=True, null=True)),
                ('ncites', models.IntegerField(blank=True, null=True)),
                ('nauthors', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'venues',
            },
        ),
        migrations.CreateModel(
            name='YearlyStat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('venue_id', models.BigIntegerField()),
                ('selfcites', models.IntegerField(blank=True, null=True)),
                ('ndocs', models.IntegerField(blank=True, null=True)),
                ('ncites', models.IntegerField(blank=True, null=True)),
                ('nauthors', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'yearly_stat',
            },
        ),
        migrations.RemoveField(
            model_name='paper',
            name='author',
        ),
        migrations.CreateModel(
            name='AcknowledgmentsVersionshadow',
            fields=[
                ('id', models.ForeignKey(serialize=False, db_column='id', primary_key=True, to='idciapp.Acknowledgments')),
                ('name', models.CharField(blank=True, null=True, max_length=100)),
                ('enttype', models.CharField(blank=True, null=True, max_length=100, db_column='entType')),
                ('acktype', models.CharField(blank=True, null=True, max_length=100, db_column='ackType')),
            ],
            options={
                'db_table': 'acknowledgments_versionshadow',
            },
        ),
        migrations.CreateModel(
            name='AuthorsVersionshadow',
            fields=[
                ('id', models.ForeignKey(serialize=False, db_column='id', primary_key=True, to='idciapp.Authors')),
                ('name', models.CharField(blank=True, null=True, max_length=100)),
                ('affil', models.CharField(blank=True, null=True, max_length=100)),
                ('address', models.CharField(blank=True, null=True, max_length=100)),
                ('email', models.CharField(blank=True, null=True, max_length=100)),
                ('ord', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'db_table': 'authors_versionshadow',
            },
        ),
        migrations.CreateModel(
            name='Citecharts',
            fields=[
                ('id', models.ForeignKey(serialize=False, db_column='id', primary_key=True, to='idciapp.Papers')),
                ('lastncites', models.IntegerField(db_column='lastNcites')),
                ('citechartdata', models.TextField(blank=True, null=True, db_column='citechartData')),
            ],
            options={
                'db_table': 'citecharts',
            },
        ),
        migrations.CreateModel(
            name='KeywordsVersionshadow',
            fields=[
                ('id', models.ForeignKey(serialize=False, db_column='id', primary_key=True, to='idciapp.Keywords')),
                ('keyword', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'db_table': 'keywords_versionshadow',
            },
        ),
        migrations.CreateModel(
            name='PapersVersionshadow',
            fields=[
                ('id', models.ForeignKey(serialize=False, db_column='id', primary_key=True, to='idciapp.Papers')),
                ('title', models.CharField(blank=True, null=True, max_length=100)),
                ('abstract', models.CharField(blank=True, null=True, max_length=100)),
                ('year', models.CharField(blank=True, null=True, max_length=100)),
                ('venue', models.CharField(blank=True, null=True, max_length=100)),
                ('venuetype', models.CharField(blank=True, null=True, max_length=100, db_column='venueType')),
                ('pages', models.CharField(blank=True, null=True, max_length=100)),
                ('volume', models.CharField(blank=True, null=True, max_length=100)),
                ('number', models.CharField(blank=True, null=True, max_length=100)),
                ('publisher', models.CharField(blank=True, null=True, max_length=100)),
                ('pubaddress', models.CharField(blank=True, null=True, max_length=100, db_column='pubAddress')),
                ('tech', models.CharField(blank=True, null=True, max_length=100)),
                ('citations', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'db_table': 'papers_versionshadow',
            },
        ),
        migrations.DeleteModel(
            name='Paper',
        ),
        migrations.AlterUniqueTogether(
            name='yearlystat',
            unique_together=set([('venue_id', 'year')]),
        ),
        migrations.AlterUniqueTogether(
            name='venuepapermap',
            unique_together=set([('paperid', 'venue_id')]),
        ),
        migrations.AddField(
            model_name='usercorrections',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='urls',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='tags',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='paperversions',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='legacyidmap',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='keywords',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='hubmap',
            name='hubid',
            field=models.ForeignKey(db_column='hubid', to='idciapp.Huburls'),
        ),
        migrations.AddField(
            model_name='hubmap',
            name='urlid',
            field=models.ForeignKey(db_column='urlid', to='idciapp.Urls'),
        ),
        migrations.AddField(
            model_name='etables',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='elinks',
            name='label',
            field=models.ForeignKey(db_column='label', to='idciapp.LinkTypes'),
        ),
        migrations.AddField(
            model_name='elinks',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='ealgorithms',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='citations',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='citationcontexts',
            name='citationid',
            field=models.ForeignKey(db_column='citationid', to='idciapp.Citations'),
        ),
        migrations.AddField(
            model_name='checksum',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='authors',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='acknowledgments',
            name='paperid',
            field=models.ForeignKey(db_column='paperid', to='idciapp.Papers'),
        ),
        migrations.AddField(
            model_name='acknowledgmentcontexts',
            name='ackid',
            field=models.ForeignKey(db_column='ackid', to='idciapp.Acknowledgments'),
        ),
        migrations.AlterUniqueTogether(
            name='elinks',
            unique_together=set([('paperid', 'label')]),
        ),
    ]
