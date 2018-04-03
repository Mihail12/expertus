from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    pass

class Project(models.Model):
    name = models.CharField(max_length=1)
    type = models.CharField(max_length=1)
    end_date = models.DateField()
    interface_config = models.CharField(max_length=1)
    description = models.TextField(max_length=4000)
    active = models.BooleanField()
    group = models.ForeignKey('ProjectGroup', on_delete=models.CASCADE)
    classification = models.ManyToManyField('Classification')


class ProjectGroup(models.Model):
    name = models.CharField(max_length=1)
    display_order = models.IntegerField()
    status = models.CharField(max_length=1)
    is_public = models.BooleanField()

class Classification(models.Model):
    strict = models.BooleanField()
    structure = models.CharField(max_length=1)
    multivalue = models.BooleanField()
    user = models.BooleanField()
    document = models.BooleanField()


