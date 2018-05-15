# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-12 15:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('useract', '0011_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthofUser',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useract.Authority')),
            ],
        ),
    ]
