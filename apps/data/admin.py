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
