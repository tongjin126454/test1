# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('atitle', models.CharField(max_length=20)),
                ('aparent', models.ForeignKey(to='booktest.AreaInfo', blank=True, null=True)),
            ],
        ),
    ]
