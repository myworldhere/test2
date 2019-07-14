# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(db_column=b'publish_date')),
                ('read', models.IntegerField(default=0)),
                ('comment', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('gender', models.BooleanField(default=False)),
                ('content', models.CharField(max_length=1000)),
                ('isDelete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
