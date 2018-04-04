from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    group = models.ManyToManyField('ProjectGroup', through='GroupUserLink')
    organization = models.ManyToManyField('Organization', through='OrganizationLink')
    project = models.ManyToManyField('Project', through='ProjectUserLink')

class Classification(models.Model):
    strict = models.BooleanField()
    structure = models.TextField(max_length=32000)
    multivalue = models.BooleanField()
    user = models.BooleanField()
    document = models.BooleanField()

class ClassificationProjectLink(models.Model):
    classification = models.ForeignKey('Classification', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1)
    end_date = models.DateField(null=True, blank=True)
    interface_config = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=4000, null=True, blank=True)
    active = models.BooleanField()
    group = models.OneToOneField('ProjectGroup', on_delete=models.CASCADE, null=True, blank=True)
    classification = models.ManyToManyField('Classification', through='ClassificationProjectLink')


class ProjectGroup(models.Model):
    name = models.CharField(max_length=255)
    display_order = models.IntegerField()
    status = models.CharField(max_length=1)
    is_public = models.BooleanField()


class ClassData(models.Model):
    classification = models.OneToOneField('ProjectGroup', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    group_user_link = models.OneToOneField('GroupUserLink', on_delete=models.CASCADE, null=True, blank=True)
    project_user_link = models.OneToOneField('ProjectUserLink', on_delete=models.CASCADE, null=True, blank=True)


class GroupUserLink(models.Model):
    moderator = models.BooleanField()
    verified = models.BooleanField()
    admin = models.BooleanField()
    participant = models.BooleanField()
    observer = models.BooleanField()
    group = models.ForeignKey('ProjectGroup', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)


class Organization(models.Model):
    name = models.CharField(max_length=255)


class OrganizationLink(models.Model):
    position = models.CharField(max_length=255)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    group_user_link = models.OneToOneField('GroupUserLink', on_delete=models.CASCADE, null=True, blank=True)
    project_user_link = models.OneToOneField('ProjectUserLink', on_delete=models.CASCADE, null=True, blank=True)


class ProjectUserLink(models.Model):
    moderator = models.BooleanField()
    verified = models.BooleanField()
    admin = models.BooleanField()
    participant = models.BooleanField()
    observer = models.BooleanField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
