# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdr_tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cdr',
            options={},
        ),
        migrations.AlterModelOptions(
            name='musiconhold',
            options={},
        ),
        migrations.AlterModelOptions(
            name='queuelog',
            options={},
        ),
        migrations.AlterModelOptions(
            name='queuemembertable',
            options={},
        ),
        migrations.AlterModelOptions(
            name='queuetable',
            options={},
        ),
        migrations.AlterModelOptions(
            name='sipdevices',
            options={},
        ),
        migrations.AlterModelOptions(
            name='voicemail',
            options={},
        ),
    ]
