# Generated by Django 3.2.15 on 2022-11-25 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_tenant_phoneno'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='plot',
            name='image',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]
