# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('prize', models.SmallIntegerField(db_column='Prize')),
                ('votesreq', models.IntegerField(db_column='VotesReq')),
            ],
            options={
                'db_table': 'Prize',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('details', models.TextField(db_column='Details')),
                ('image', models.CharField(db_column='Image', max_length=256)),
                ('date', models.DateTimeField(db_column='Date')),
            ],
            options={
                'db_table': 'Story',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Storycomment',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('comment', models.TextField(db_column='Comment')),
                ('date', models.DateTimeField(db_column='Date')),
                ('approved', models.NullBooleanField(db_column='Approved')),
            ],
            options={
                'db_table': 'StoryComment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=256)),
                ('details', models.TextField(db_column='Details')),
                ('date', models.DateField(db_column='Date')),
                ('publish_date', models.DateField(blank=True, db_column='Publish_Date', null=True)),
                ('vcounts', models.IntegerField(blank=True, db_column='Vcounts', null=True)),
            ],
            options={
                'db_table': 'Trip',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tripcomment',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('comment', models.TextField(db_column='Comment')),
                ('date', models.DateTimeField(db_column='Date')),
                ('approved', models.NullBooleanField(db_column='Approved')),
            ],
            options={
                'db_table': 'TripComment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userprize',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='Date')),
            ],
            options={
                'db_table': 'UserPrize',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('profileid', models.AutoField(db_column='ProfileId', primary_key=True, serialize=False)),
                ('profilepic', models.CharField(blank=True, db_column='ProfilePic', max_length=256, null=True)),
            ],
            options={
                'db_table': 'UserProfile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(db_column='Date')),
            ],
            options={
                'db_table': 'Vote',
                'managed': False,
            },
        ),
    ]