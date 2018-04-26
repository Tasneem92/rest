# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class Prize(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    prize = models.SmallIntegerField(db_column='Prize')  # Field name made lowercase.
    votesreq = models.IntegerField(db_column='VotesReq')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prize'


class Story(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    details = models.TextField(db_column='Details')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=256)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    tripid = models.ForeignKey('Trip', models.DO_NOTHING, db_column='TripId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Story'


class Storycomment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    bloggerid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='BloggerId')  # Field name made lowercase.
    storyid = models.ForeignKey(Story, models.DO_NOTHING, db_column='StoryId')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    approved = models.NullBooleanField(db_column='Approved')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoryComment'


class Trip(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=256)  # Field name made lowercase.
    details = models.TextField(db_column='Details')  # Field name made lowercase.
    bloggerid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='BloggerId')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    publish_date = models.DateField(db_column='Publish_Date', blank=True, null=True)  # Field name made lowercase.
    vcounts = models.IntegerField(db_column='Vcounts', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Trip'

    def get_absolute_url(self):
        return reverse("trip_detail",kwargs={'pk':self.pk})

class Tripcomment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    bloggerid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='BloggerId')  # Field name made lowercase.
    tripid = models.ForeignKey(Trip, models.DO_NOTHING, db_column='TripId')  # Field name made lowercase.
    approved = models.NullBooleanField(db_column='Approved')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TripComment'

    def get_absolute_url(self):
        return reverse("trip_detail",kwargs={'pk':self.tripid.pk})

class Userprize(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    bloggerid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='BloggerId')  # Field name made lowercase.
    tripid = models.ForeignKey(Trip, models.DO_NOTHING, db_column='TripId')  # Field name made lowercase.
    prizeid = models.ForeignKey(Prize, models.DO_NOTHING, db_column='PrizeId')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserPrize'


class Userprofile(models.Model):
    profileid = models.AutoField(db_column='ProfileId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    profilepic = models.ImageField(db_column='ProfilePic',upload_to='profile_pics', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserProfile'


class Vote(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    bloggerid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='BloggerId')  # Field name made lowercase.
    tripid = models.ForeignKey(Trip, models.DO_NOTHING, db_column='TripId')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vote'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
