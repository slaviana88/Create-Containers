# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name_owner', models.CharField(unique=True, max_length=50)),
                ('name_container', models.CharField(null=True, blank=True, max_length=50)),
                ('ssh_key', models.CharField(max_length=1000)),
                ('status', models.CharField(default='waiting', max_length=8)),
                ('container_ip', models.CharField(null=True, blank=True, max_length=15)),
            ],
        ),
    ]
