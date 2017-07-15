# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0003_auto_20170715_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='person1',
            name='game_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person2',
            name='game_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person2',
            name='playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person3',
            name='game_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person3',
            name='playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person4',
            name='game_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person4',
            name='playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person5',
            name='game_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person5',
            name='playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person6',
            name='game_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person6',
            name='playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person7',
            name='game_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person7',
            name='playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person8',
            name='game_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person8',
            name='playing',
            field=models.BooleanField(default=False),
        ),
    ]
