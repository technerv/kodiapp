# Generated by Django 3.2.15 on 2022-12-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20221210_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account_type',
        ),
        migrations.AddField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(default=False, verbose_name='Plot/Land Owner'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_tenant',
            field=models.BooleanField(default=False, verbose_name='Tenant'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='superuser status'),
        ),
    ]