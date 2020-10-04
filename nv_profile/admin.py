from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm

from nv_profile.models import NVUserProfile, NVRoom, NVSkill, UserSkills
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin

admin.site.unregister(models.Group)

class UserSkillInLine(admin.TabularInline):
    model = UserSkills

@admin.register(NVUserProfile)
class UserAdmin(OriginalUserAdmin):
    list_display = ('username', 'current_room')
    list_filter = ('current_room',)
    filter_horizontal = ()
    inlines = [UserSkillInLine]
    fieldsets = (
        (None, {'fields': ('id','username', 'email')}),
        (_('Personal info'), {'fields': ('name', 'is_male', 'current_room', 'last_active_room')}),
        # (_('Skills'), {'fields': ('skills',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'password1', 'password2'),  # not to touch this
        }),
    )
    readonly_fields = ('id', 'last_active_room', 'current_room')


@admin.register(NVRoom)
class NVRoomAdmin(admin.ModelAdmin):
    pass

@admin.register(NVSkill)
class NVSkillAdmin(admin.ModelAdmin):
    pass

