# Generated by Django 3.1.1 on 2020-09-24 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0008_unit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='remarks',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Remarks'),
        ),
    ]
