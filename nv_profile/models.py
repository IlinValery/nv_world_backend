from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, User, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class NVRoom(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    sprite = models.FileField(upload_to='rooms')

    def __str__(self):
        return str(self.title)


class NVSkill(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return str(self.title)


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_unusable_password()


        user.save()

        return user

    def _create_super_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_unusable_password()
        # user.set_password(password)
        user.save()
        return user

    def create_user(self, username, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        print(extra_fields)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_super_user(username=username, password=password, **extra_fields)


class NVUserProfile(AbstractUser):
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    email = models.EmailField(_('email address'), blank=True, null=True)
    name = models.CharField(max_length=255, blank=False)
    photo = models.ImageField(upload_to='user_photos')

    is_team_lead = models.BooleanField(default=False)
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
