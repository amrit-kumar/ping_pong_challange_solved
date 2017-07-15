# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0004_auto_20170715_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentPlayerList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_list', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
