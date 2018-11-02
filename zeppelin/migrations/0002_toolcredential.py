# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-26 00:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zeppelin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToolCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=150, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zeppelin.Tool')),
            ],
        ),
    ]