# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20181116_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketingpreference',
            name='mailchimp_subscribed',
        ),
    ]
