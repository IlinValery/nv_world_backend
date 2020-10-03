from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm

from nv_profile.models import NVUserProfile, NVRoom, NVSkill
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin

admin.site.unregister(models.Group)


@admin.register(NVUserProfile)
class UserAdmin(OriginalUserAdmin):
    list_display = ('username', 'current_room')
    list_filter = ('current_room',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        (_('Personal info'), {'fields': ('name', 'current_room')}),
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


@admin.register(NVRoom)
class NVRoomAdmin(admin.ModelAdmin):
    pass
