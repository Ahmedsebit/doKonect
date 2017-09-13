# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_referral', '0002_auto_20170903_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_referral',
            name='booked_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='doctor_referral',
            name='comments',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='doctor_referral',
            name='group',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_referral',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='doctor_referral',
            name='doctor_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor_referral',
            name='patient_id',
            field=models.CharField(max_length=50),
        ),
    ]