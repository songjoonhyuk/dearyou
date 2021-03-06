# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sender', models.CharField(max_length=50)),
                ('recipient', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('address_sender', models.TextField()),
                ('address_recipient', models.TextField()),
                ('phone_sender', models.CharField(max_length=20)),
                ('phone_recipient', models.CharField(max_length=20)),
            ],
        ),
    ]
