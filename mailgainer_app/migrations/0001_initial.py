# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-23 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=30, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('birth_date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442',
                'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
            },
        ),
    ]