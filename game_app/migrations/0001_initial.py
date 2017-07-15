# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player1_id', models.IntegerField(null=True)),
                ('player2_id', models.IntegerField(null=True)),
                ('player1_responses', models.CharField(max_length=200)),
                ('player2_responses', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('order', models.IntegerField()),
                ('round_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('defence_len', models.IntegerField()),
                ('joined', models.IntegerField(default=0)),
                ('tour_status', models.IntegerField(default=0)),
                ('round1_gameid', models.IntegerField(null=True)),
                ('round1_qualified', models.IntegerField(null=True)),
                ('round2_gameid', models.IntegerField(null=True)),
                ('round2_qualified', models.IntegerField(null=True)),
                ('round3_gameid', models.IntegerField(null=True)),
                ('round3_winner', models.IntegerField(null=True)),
                ('uid', models.ForeignKey(related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=1)),
                ('x', models.CharField(default=b'[1,2,3,4,5,6,7,8]', max_length=50)),
            ],
        ),
    ]
