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
            name='Person1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playing', models.BooleanField(default=False)),
                ('game_number', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, max_length=10, null=True, choices=[(b'attacker', b'ATTACKER'), (b'defencer', b'DEFENCER')])),
                ('defense_array', models.TextField(null=True, blank=True)),
                ('attack_array', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playing', models.BooleanField(default=False)),
                ('game_number', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, max_length=10, null=True, choices=[(b'attacker', b'ATTACKER'), (b'defencer', b'DEFENCER')])),
                ('defense_array', models.TextField(null=True, blank=True)),
                ('attack_array', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playing', models.BooleanField(default=False)),
                ('game_number', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, max_length=10, null=True, choices=[(b'attacker', b'ATTACKER'), (b'defencer', b'DEFENCER')])),
                ('defense_array', models.TextField(null=True, blank=True)),
                ('attack_array', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playing', models.BooleanField(default=False)),
                ('game_number', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, max_length=10, null=True, choices=[(b'attacker', b'ATTACKER'), (b'defencer', b'DEFENCER')])),
                ('defense_array', models.TextField(null=True, blank=True)),
                ('attack_array', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playing', models.BooleanField(default=False)),
                ('game_number', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, max_length=10, null=True, choices=[(b'attacker', b'ATTACKER'), (b'defencer', b'DEFENCER')])),
                ('defense_array', models.TextField(null=True, blank=True)),
                ('attack_array', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person6',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playing', models.BooleanField(default=False)),
                ('game_number', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, max_length=10, null=True, choices=[(b'attacker', b'ATTACKER'), (b'defencer', b'DEFENCER')])),
                ('defense_array', models.TextField(null=True, blank=True)),
                ('attack_array', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person7',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playing', models.BooleanField(default=False)),
                ('game_number', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, max_length=10, null=True, choices=[(b'attacker', b'ATTACKER'), (b'defencer', b'DEFENCER')])),
                ('defense_array', models.TextField(null=True, blank=True)),
                ('attack_array', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person8',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playing', models.BooleanField(default=False)),
                ('game_number', models.IntegerField(default=0)),
                ('point', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, max_length=10, null=True, choices=[(b'attacker', b'ATTACKER'), (b'defencer', b'DEFENCER')])),
                ('defense_array', models.TextField(null=True, blank=True)),
                ('attack_array', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_won', models.CharField(max_length=50)),
            ],
        ),
    ]
