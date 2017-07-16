# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentPlayerList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_list', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('player_won', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('playing', models.BooleanField(default=False)),
                ('game_number', models.IntegerField(default=0)),
                ('game_id', models.IntegerField()),
                ('array_length', models.IntegerField()),
                ('point', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, max_length=10, null=True, choices=[(b'attacker', b'ATTACKER'), (b'defencer', b'DEFENCER')])),
                ('defense_array', models.TextField(null=True, blank=True)),
                ('attack_array', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
