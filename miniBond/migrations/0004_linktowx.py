# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-22 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniBond', '0003_auto_20170921_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkToWx',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('wxText', models.TextField()),
                ('platForm', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='miniBond.Platform')),
            ],
        ),
    ]
