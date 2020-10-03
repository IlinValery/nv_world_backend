from django.db import models
from nv_profile.models import NVUserProfile, NVSkill, NVRoom
from django.utils.translation import gettext_lazy as _


class NVProject(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=False, null=False)
    person_in_charge = models.OneToOneField(NVUserProfile, blank=True, null=True, on_delete=models.CASCADE)
    parent_project = models.OneToOneField('self', blank=True, null=True, on_delete=models.CASCADE)
    room = models.OneToOneField(NVRoom, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self):
        return str(self.name)


class RolesInProject(models.Model):
    user = models.ForeignKey(NVUserProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(NVProject, on_delete=models.CASCADE)

    class RolesInProject(models.TextChoices):
        PROJECTMANAGER = 'PM', _('Project manager')
        ANALYST = 'AL', _('Analyst')
        LEADANALYST = 'LA', _('Lead Analyst')
        ARCHITECT = 'AT', _('Architect')
        TEAMLEAD = 'TL', _('Team lead')
        DEVELOPER = 'DV', _('Developer')
        QUALITYASSURANCE = 'QA', _('Quality Assurance')
        SYSADMIN = 'SA', _('System Administrator')

    role = models.CharField(
        max_length=2,
        choices=RolesInProject.choices,
        default=RolesInProject.DEVELOPER,
    )


class NVTask(models.Model):
    user = models.ForeignKey(NVUserProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(NVProject, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(NVSkill, blank=True)
    is_open = models.BooleanField(default=True)

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"


class NVOpenPosition(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    is_open = models.BooleanField(default=True)
    project = models.ForeignKey(NVProject, on_delete=models.CASCADE)
    skills = models.ManyToManyField(NVSkill)

    class Meta:
        verbose_name = "open position"
        verbose_name_plural = "open positions"

    def __str__(self):
        return str(self.name)


class NVIdea(models.Model):
    subject = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(NVProject, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(NVUserProfile, on_delete=models.CASCADE, blank=False, null=False)
    in_archive = models.BooleanField(default=False)

    class Meta:
        verbose_name = "idea"
        verbose_name_plural = "ideas"

    def __str__(self):
        return str(self.subject)


class IdeaVotes(models.Model):
    idea = models.ForeignKey(NVIdea, on_delete=models.CASCADE)
    user = models.ForeignKey(NVUserProfile, on_delete=models.CASCADE)
    is_positive = models.BooleanField()


class IdeaComment(models.Model):
    idea = models.ForeignKey(NVIdea, on_delete=models.CASCADE)
    user = models.ForeignKey(NVUserProfile, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
