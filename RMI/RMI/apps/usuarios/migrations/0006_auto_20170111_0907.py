# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-11 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20170111_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte_mensual',
            name='adjunto_exel',
            field=models.FileField(default='reporte.xls', upload_to='Reporte/'),
        ),
    ]
