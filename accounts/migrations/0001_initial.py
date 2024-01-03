# Generated by Django 3.2.15 on 2022-12-02 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('salutation', models.CharField(choices=[('MR', 'MR'), ('MRS', 'MRS'), ('MISS', 'MISS')], max_length=8, verbose_name='Salutation')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('confirmed_email', models.BooleanField(default=False)),
                ('mobile_number', models.CharField(max_length=20)),
                ('is_owner', models.BooleanField(default=False, verbose_name='Plot/Land Owner')),
                ('is_tenant', models.BooleanField(default=False, verbose_name='Tenant')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('activation_key', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-date_updated',),
            },
        ),
    ]
