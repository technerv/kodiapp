# Generated by Django 3.2.15 on 2022-11-21 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221121_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='name',
        ),
    ]
