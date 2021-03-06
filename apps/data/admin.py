from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User, UserAdmin)
admin.site.register(Classification)
admin.site.register(ClassificationProjectLink)
admin.site.register(Project)
admin.site.register(ProjectGroup)
admin.site.register(ClassData)
admin.site.register(GroupUserLink)
admin.site.register(Organization)
admin.site.register(OrganizationLink)
admin.site.register(ProjectUserLink)
admin.site.register(Problem)
admin.site.register(Measure)
admin.site.register(Solution)
admin.site.register(Document)
admin.site.register(Section)
admin.site.register(Suggestion)
admin.site.register(Estimation)
admin.site.register(ProjectVocabularyLink)
admin.site.register(Vocabulary)
admin.site.register(Term)
admin.site.register(Attachment)
admin.site.register(Resource)
admin.site.register(Comment)
