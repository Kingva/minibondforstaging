# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-21 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniBond', '0002_auto_20170811_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelText',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformLabel',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('label', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='miniBond.LabelText')),
                ('platForm', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='miniBond.Platform')),
            ],
        ),
        migrations.AddField(
            model_name='promotioninfo',
            name='idValid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='platformrating',
            name='platForm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniBond.Platform'),
        ),
        migrations.AlterField(
            model_name='platformrating',
            name='ratingOrganization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniBond.RatingOrganization'),
        ),
        migrations.AlterField(
            model_name='promotioninfo',
            name='platForm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniBond.Platform'),
        ),
        migrations.AlterField(
            model_name='promotioninfo',
            name='promotionAgency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniBond.PromotionAgency'),
        ),
    ]
