# Generated by Django 3.2.15 on 2022-12-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_owner',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_tenant',
        ),
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('Plot Owner', 'Plot Owner'), ('Tenant', 'Tenant')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
