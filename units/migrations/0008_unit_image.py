# Generated by Django 3.1.1 on 2020-09-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0007_auto_20200923_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='units_images/', verbose_name='Unit Main Image'),
        ),
    ]
