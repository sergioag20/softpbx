# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spw_display_name', models.CharField(unique=True, max_length=80, verbose_name='Display name', db_index=True)),
                ('spw_username', models.IntegerField(unique=True, verbose_name='Username')),
                ('spw_passwd', models.CharField(max_length=80, verbose_name='Password')),
                ('spw_email', models.EmailField(max_length=150, null=True, verbose_name='E-mail', blank=True)),
                ('spw_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'db_table': 'spw_ramais',
                'verbose_name': 'Extension',
                'verbose_name_plural': 'Extension',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupExtension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spw_group_name', models.CharField(unique=True, max_length=80, verbose_name='Group name')),
                ('spw_group_type', models.IntegerField(verbose_name='Group type', choices=[(1, 'Call Group'), (2, 'Pick up Group')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='extension',
            name='spw_call_group',
            field=models.ForeignKey(related_name='call_group', to='spw_extension.GroupExtension'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extension',
            name='spw_pickup_group',
            field=models.ForeignKey(related_name='pick_up_group', to='spw_extension.GroupExtension'),
            preserve_default=True,
        ),
    ]
