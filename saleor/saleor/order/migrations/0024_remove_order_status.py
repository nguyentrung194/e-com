# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-14 11:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("order", "0023_auto_20171206_0506")]

    operations = [migrations.RemoveField(model_name="order", name="status")]
