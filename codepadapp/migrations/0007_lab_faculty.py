# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codepadapp', '0006_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='Faculty',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='codepadapp.Faculty'),
            preserve_default=False,
        ),
    ]
