from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, User, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from nv_profile.manager import CustomUserManager


class NVRoom(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    link = models.CharField(max_length=255, blank=True, null=True)
    sprite = models.FileField(upload_to='rooms')

    class Meta:
        verbose_name = "room"
        verbose_name_plural = "rooms"

    def __str__(self):
        return str(self.title)


class NVSkill(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = "skill"
        verbose_name_plural = "skills"

    def __str__(self):
        return str(self.title)


class NVUserProfile(AbstractUser):
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    email = models.EmailField(_('email address'), blank=True, null=True)
    name = models.CharField(max_length=255, blank=False)
    photo = models.ImageField(upload_to='user_photos')

    is_team_lead = models.BooleanField(default=False)
    is_male = models.BooleanField(default=True)
    cartoon_sprite = models.FileField(upload_to='user_avatars', blank=True, null=True)

    report_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    current_room = models.ForeignKey(NVRoom, on_delete=models.CASCADE, blank=True, null=True)
    skills = models.ManyToManyField(NVSkill, through='UserSkills')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)


class UserSkills(models.Model):
    user = models.ForeignKey(NVUserProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(NVSkill, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    is_majority = models.BooleanField(default=False)
