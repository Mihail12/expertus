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
    vocabulary = models.ManyToManyField('Vocabulary', through='ProjectVocabularyLink')


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


class Problem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=16000)
    type = models.CharField(max_length=1)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    measure = models.ForeignKey('Measure', on_delete=models.CASCADE)


class Measure(models.Model):
    description = models.TextField(max_length=16000)
    structure = models.TextField(max_length=16000)


class Solution(models.Model):
    type = models.CharField(max_length=1)
    body = models.TextField(max_length=16000, null=True, blank=True)
    title = models.CharField(max_length=255)
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)


class Document(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class Section(models.Model):
    type = models.CharField(max_length=1)
    text = models.TextField(max_length=1050000, null=True, blank=True)
    ancestry = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField()
    document = models.ForeignKey('Document', on_delete=models.CASCADE)


class Suggestion(models.Model):
    type = models.CharField(max_length=1)
    text = models.TextField(max_length=1050000, null=True, blank=True)
    explanation = models.TextField(max_length=4000)
    ancestry = models.CharField(max_length=255, null=True, blank=True)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)


class Estimation(models.Model):
    value = models.CharField(max_length=255)
    measure = models.ForeignKey('Measure', on_delete=models.CASCADE)
    solution = models.OneToOneField('Solution', on_delete=models.CASCADE, null=True, blank=True)
    suggestion = models.OneToOneField('Suggestion', on_delete=models.CASCADE, null=True, blank=True)


class ProjectVocabularyLink(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    vocabulary = models.ForeignKey('Vocabulary', on_delete=models.CASCADE)


class Vocabulary(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    extendable = models.BooleanField()
    public = models.BooleanField()


class Term(models.Model):
    name_ua = models.CharField(max_length=255)
    description_ua = models.TextField(max_length=4000)
    description_ru = models.TextField(max_length=4000)
    description_en = models.TextField(max_length=4000)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    vocabulary = models.ForeignKey('Vocabulary', on_delete=models.CASCADE)


class Attachment(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    content_type = models.TextField()
    filename = models.CharField(max_length=255)
    solution = models.ForeignKey('Solution', on_delete=models.CASCADE)
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE)
    measure = models.ForeignKey('Measure', on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    term = models.ForeignKey('Term', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    vocabulary = models.ForeignKey('Vocabulary', on_delete=models.CASCADE)
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    suggestion = models.ForeignKey('Suggestion', on_delete=models.CASCADE)
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)


class Resource(models.Model):
    text = models.TextField(max_length=1050000, null=True, blank=True)
    type = models.CharField(max_length=1)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    solution = models.ForeignKey('Solution', on_delete=models.CASCADE)
    suggestion = models.ForeignKey('Suggestion', on_delete=models.CASCADE)
    vocabulary = models.ForeignKey('Vocabulary', on_delete=models.CASCADE)
    measure = models.ForeignKey('Measure', on_delete=models.CASCADE)


class Comment(models.Model):
    type = models.CharField(max_length=1, null=True, blank=True)
    ancestry = models.CharField(max_length=255, null=True, blank=True)
    solution = models.ForeignKey('Solution', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    vocabulary = models.ForeignKey('Vocabulary', on_delete=models.CASCADE)
    measure = models.ForeignKey('Measure', on_delete=models.CASCADE)
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    suggestion = models.ForeignKey('Suggestion', on_delete=models.CASCADE)
    term = models.ForeignKey('Term', on_delete=models.CASCADE)
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE)
