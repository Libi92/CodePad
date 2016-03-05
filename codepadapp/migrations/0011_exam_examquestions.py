# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codepadapp', '0010_userprograms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examname', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codepadapp.Lab')),
            ],
        ),
        migrations.CreateModel(
            name='ExamQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1024)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codepadapp.Exam')),
            ],
        ),
    ]
