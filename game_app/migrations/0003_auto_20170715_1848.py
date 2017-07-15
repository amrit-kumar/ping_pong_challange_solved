# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0002_auto_20170715_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person2',
            fields=[
                ('personmixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='game_app.PersonMixin')),
            ],
            bases=('game_app.personmixin', models.Model),
        ),
        migrations.CreateModel(
            name='Person3',
            fields=[
                ('personmixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='game_app.PersonMixin')),
            ],
            bases=('game_app.personmixin', models.Model),
        ),
        migrations.CreateModel(
            name='Person4',
            fields=[
                ('personmixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='game_app.PersonMixin')),
            ],
            bases=('game_app.personmixin', models.Model),
        ),
        migrations.CreateModel(
            name='Person5',
            fields=[
                ('personmixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='game_app.PersonMixin')),
            ],
            bases=('game_app.personmixin', models.Model),
        ),
        migrations.CreateModel(
            name='Person6',
            fields=[
                ('personmixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='game_app.PersonMixin')),
            ],
            bases=('game_app.personmixin', models.Model),
        ),
        migrations.CreateModel(
            name='Person7',
            fields=[
                ('personmixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='game_app.PersonMixin')),
            ],
            bases=('game_app.personmixin', models.Model),
        ),
        migrations.CreateModel(
            name='Person8',
            fields=[
                ('personmixin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='game_app.PersonMixin')),
            ],
            bases=('game_app.personmixin', models.Model),
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_won', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='person1',
            name='playing',
            field=models.BooleanField(default=False),
        ),
    ]
