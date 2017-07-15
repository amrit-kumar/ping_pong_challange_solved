# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonMixin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, max_length=10, null=True, choices=[(b'attacker', b'ATTACKER'), (b'defencer', b'DEFENCER')])),
                ('defense_array', models.TextField(null=True, blank=True)),
                ('attack_array', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.RemoveField(
            model_name='players',
            name='uid',
        ),
        migrations.DeleteModel(
            name='Variables',
        ),
        migrations.CreateModel(
            name='Person1',
            fields=[
                ('personmixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='game_app.PersonMixin')),
            ],
            bases=('game_app.personmixin', models.Model),
        ),
        migrations.DeleteModel(
            name='Players',
        ),
    ]
