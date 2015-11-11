# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `#managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Acknowledgmentcontexts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ackid = models.ForeignKey('Acknowledgments', db_column='ackid')
    context = models.TextField()

    class Meta:
        #managed = False
        db_table = 'acknowledgmentcontexts'


class Acknowledgments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cluster = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    enttype = models.CharField(db_column='entType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    acktype = models.CharField(db_column='ackType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paperid = models.ForeignKey('Papers', db_column='paperid')

    class Meta:
        #managed = False
        db_table = 'acknowledgments'


class AcknowledgmentsVersionshadow(models.Model):
    id = models.ForeignKey(Acknowledgments, db_column='id', primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    enttype = models.CharField(db_column='entType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    acktype = models.CharField(db_column='ackType', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'acknowledgments_versionshadow'


class Affilauthmap(models.Model):
    id = models.BigIntegerField(primary_key=True)
    affiliations_id = models.BigIntegerField(blank=True, null=True)
    authors_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'affilauthmap'


class Affiliations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    ncites = models.IntegerField(blank=True, null=True)
    nauthors = models.IntegerField(blank=True, null=True)
    ndocs = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'affiliations'


class Authors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cluster = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    affil = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    ord = models.IntegerField()
    paperid = models.ForeignKey('Papers', db_column='paperid')

    class Meta:
        #managed = False
        db_table = 'authors'


class AuthorsVersionshadow(models.Model):
    id = models.ForeignKey(Authors, db_column='id', primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    affil = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    ord = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'authors_versionshadow'


class Authorsaffil(models.Model):
    id = models.BigIntegerField(primary_key=True)
    authors_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'authorsaffil'


class Cannames(models.Model):
    id = models.BigIntegerField(primary_key=True)
    canname = models.CharField(max_length=100, blank=True, null=True)
    ndocs = models.IntegerField(blank=True, null=True)
    ncites = models.IntegerField()
    url = models.CharField(max_length=250, blank=True, null=True)
    affil = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    hindex = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'cannames'


class Checksum(models.Model):
    sha1 = models.CharField(primary_key=True, max_length=100)
    paperid = models.ForeignKey('Papers', db_column='paperid')
    filetype = models.CharField(max_length=10)

    class Meta:
        #managed = False
        db_table = 'checksum'


class Citationcontexts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    citationid = models.ForeignKey('Citations', db_column='citationid')
    context = models.TextField()

    class Meta:
        #managed = False
        db_table = 'citationcontexts'


class Citations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cluster = models.BigIntegerField(blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True, null=True)
    venuetype = models.CharField(db_column='venueType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    pages = models.CharField(max_length=20, blank=True, null=True)
    editors = models.TextField(blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    pubaddress = models.CharField(db_column='pubAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    volume = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    tech = models.CharField(max_length=100, blank=True, null=True)
    raw = models.TextField(blank=True, null=True)
    paperid = models.ForeignKey('Papers', db_column='paperid')
    self = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'citations'


class Citecharts(models.Model):
    id = models.ForeignKey('Papers', db_column='id', primary_key=True)
    lastncites = models.IntegerField(db_column='lastNcites')  # Field name made lowercase.
    citechartdata = models.TextField(db_column='citechartData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'citecharts'


class Deletes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    table_id = models.BigIntegerField(blank=True, null=True)
    deleted_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'deletes'


class Ealgorithms(models.Model):
    id = models.BigIntegerField(primary_key=True)
    proxyid = models.CharField(db_column='proxyID', max_length=100)  # Field name made lowercase.
    caption = models.CharField(max_length=500, blank=True, null=True)
    synopsis = models.CharField(max_length=2000, blank=True, null=True)
    reftext = models.CharField(max_length=500, blank=True, null=True)
    paperid = models.ForeignKey('Papers', db_column='paperid')
    pagenum = models.IntegerField(db_column='pageNum')  # Field name made lowercase.
    ncites = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'ealgorithms'


class Elinks(models.Model):
    paperid = models.ForeignKey('Papers', db_column='paperid')
    label = models.ForeignKey('LinkTypes', db_column='label')
    url = models.CharField(max_length=255)

    class Meta:
        #managed = False
        db_table = 'elinks'
        unique_together = (('paperid', 'label'),)


class Etables(models.Model):
    id = models.BigIntegerField(primary_key=True)
    proxyid = models.CharField(db_column='proxyID', max_length=100)  # Field name made lowercase.
    indocid = models.IntegerField(db_column='inDocID', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    footnote = models.CharField(db_column='footNote', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reftext = models.CharField(db_column='refText', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paperid = models.ForeignKey('Papers', db_column='paperid')
    pagenum = models.IntegerField(db_column='pageNum')  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='updateTime')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'etables'


class Hubmap(models.Model):
    id = models.BigIntegerField(primary_key=True)
    urlid = models.ForeignKey('Urls', db_column='urlid')
    hubid = models.ForeignKey('Huburls', db_column='hubid')

    class Meta:
        #managed = False
        db_table = 'hubmap'


class Huburls(models.Model):
    id = models.BigIntegerField(primary_key=True)
    url = models.CharField(unique=True, max_length=255)
    lastcrawl = models.DateTimeField(db_column='lastCrawl')  # Field name made lowercase.
    repositoryid = models.CharField(db_column='repositoryID', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'huburls'


class Journals(models.Model):
    id = models.BigIntegerField(primary_key=True)
    venue_id = models.BigIntegerField()
    volume = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'journals'


class Keywords(models.Model):
    id = models.BigIntegerField(primary_key=True)
    keyword = models.CharField(max_length=100)
    paperid = models.ForeignKey('Papers', db_column='paperid')

    class Meta:
        #managed = False
        db_table = 'keywords'


class KeywordsVersionshadow(models.Model):
    id = models.ForeignKey(Keywords, db_column='id', primary_key=True)
    keyword = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'keywords_versionshadow'


class Legacyidmap(models.Model):
    id = models.BigIntegerField(primary_key=True)
    paperid = models.ForeignKey('Papers', db_column='paperid')
    legacyid = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'legacyidmap'


class LinkTypes(models.Model):
    label = models.CharField(primary_key=True, max_length=50)
    baseurl = models.CharField(db_column='baseURL', max_length=255)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'link_types'


class Papers(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    version = models.IntegerField()
    cluster = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    venue = models.CharField(max_length=100, blank=True, null=True)
    venuetype = models.CharField(db_column='venueType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(max_length=20, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    pubaddress = models.CharField(db_column='pubAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tech = models.CharField(max_length=100, blank=True, null=True)
    public = models.IntegerField()
    ncites = models.IntegerField()
    versionname = models.CharField(db_column='versionName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    crawldate = models.DateTimeField(db_column='crawlDate')  # Field name made lowercase.
    repositoryid = models.CharField(db_column='repositoryID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    conversiontrace = models.CharField(db_column='conversionTrace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selfcites = models.IntegerField(db_column='selfCites')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='versionTime')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'papers'


class PapersVersionshadow(models.Model):
    id = models.ForeignKey(Papers, db_column='id', primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    abstract = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    venue = models.CharField(max_length=100, blank=True, null=True)
    venuetype = models.CharField(db_column='venueType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(max_length=100, blank=True, null=True)
    volume = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    pubaddress = models.CharField(db_column='pubAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tech = models.CharField(max_length=100, blank=True, null=True)
    citations = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'papers_versionshadow'


class Paperversions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    paperid = models.ForeignKey(Papers, db_column='paperid')
    version = models.IntegerField()
    repositoryid = models.CharField(db_column='repositoryID', max_length=15)  # Field name made lowercase.
    path = models.CharField(max_length=255)
    deprecated = models.IntegerField()
    spam = models.IntegerField()
    time = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'paperversions'


class Tags(models.Model):
    id = models.BigIntegerField(primary_key=True)
    paperid = models.ForeignKey(Papers, db_column='paperid')
    tag = models.CharField(max_length=50)
    count = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'tags'


class Textsources(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    content = models.TextField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'textsources'


class Urls(models.Model):
    id = models.BigIntegerField(primary_key=True)
    url = models.CharField(max_length=255)
    paperid = models.ForeignKey(Papers, db_column='paperid')

    class Meta:
        #managed = False
        db_table = 'urls'


class Usercorrections(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.CharField(max_length=100)
    paperid = models.ForeignKey(Papers, db_column='paperid')
    version = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'usercorrections'


class Users(models.Model):
    userid = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=255)
    firstname = models.CharField(db_column='firstName', max_length=100)  # Field name made lowercase.
    middlename = models.CharField(db_column='middleName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=100)  # Field name made lowercase.
    email = models.CharField(max_length=100)
    affil1 = models.CharField(max_length=255, blank=True, null=True)
    affil2 = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.IntegerField()
    country = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    webpage = models.CharField(db_column='webPage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    internalid = models.BigIntegerField()
    updated = models.DateTimeField()
    appid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ##managed = False
        db_table = 'users'


class Venuepapermap(models.Model):
    paperid = models.CharField(max_length=20)
    venue_id = models.BigIntegerField()
    venue_varname = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ##managed = False
        db_table = 'venuepapermap'
        unique_together = (('paperid', 'venue_id'),)


class Venues(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    editor = models.CharField(max_length=500, blank=True, null=True)
    issn = models.CharField(max_length=50, blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    halflife_cited = models.FloatField(blank=True, null=True)
    halflife_citing = models.FloatField(blank=True, null=True)
    impact_factor = models.FloatField(blank=True, null=True)
    immediciacy = models.FloatField(blank=True, null=True)
    hindex = models.FloatField(blank=True, null=True)
    selfcites = models.IntegerField(blank=True, null=True)
    ndocs = models.IntegerField(blank=True, null=True)
    ncites = models.IntegerField(blank=True, null=True)
    nauthors = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'venues'


class YearlyStat(models.Model):
    venue_id = models.BigIntegerField()
    selfcites = models.IntegerField(blank=True, null=True)
    ndocs = models.IntegerField(blank=True, null=True)
    ncites = models.IntegerField(blank=True, null=True)
    nauthors = models.IntegerField(blank=True, null=True)
    year = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'yearly_stat'
        unique_together = (('venue_id', 'year'),)
