# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-16 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_platform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Property', max_length=100)),
                ('slug', models.CharField(blank=True, max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='rooms_pictures')),
                ('description', models.TextField(default='Description', max_length=500)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('street_address', models.CharField(max_length=150)),
                ('suburb', models.CharField(max_length=150)),
                ('published', models.BooleanField(default=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_manager', to='core_platform.RoomManager')),
            ],
        ),
    ]
