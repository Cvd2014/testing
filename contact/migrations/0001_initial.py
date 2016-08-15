# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('sender', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2016, 8, 15, 11, 30, 19, 664000, tzinfo=utc))),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
    ]
