from django.contrib import admin

# Register your models here.
from nv_projects.models import NVProject, NVTask, NVIdea, NVOpenPosition, RolesInProject


class AdminTeamInLine(admin.TabularInline):
    model = RolesInProject


@admin.register(NVProject)
class AdminProject(admin.ModelAdmin):
    inlines = [AdminTeamInLine]


@admin.register(NVTask)
class AdminTask(admin.ModelAdmin):
    pass


@admin.register(NVIdea)
class AdminIdea(admin.ModelAdmin):
    pass


@admin.register(NVOpenPosition)
class AdminOpenPosition(admin.ModelAdmin):
    pass
