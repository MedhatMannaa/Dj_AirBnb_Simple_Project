# Generated by Django 3.1.1 on 2020-09-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='furniture',
        ),
        migrations.AddField(
            model_name='unit',
            name='furniture',
            field=models.ManyToManyField(to='units.Furniture'),
        ),
    ]