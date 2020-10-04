from abc import ABC

from rest_framework import serializers

from nv_profile.models import NVUserProfile, NVSkill, UserSkills, NVRoom
from nv_projects.models import RolesInProject, NVProject


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = NVRoom
        fields = ['id', 'title', 'sprite']


class UserSerializer(serializers.ModelSerializer):
    room_info = RoomSerializer(source='current_room')
    class Meta:
        model = NVUserProfile
        fields = ['username', 'name', 'is_male', 'email', 'photo', 'current_room', 'room_info']


class ProjectSerializerShot(serializers.ModelSerializer):
    class Meta:
        model = NVProject
        fields = ['id', 'name', 'link']


class UserRolesInTeamSerializer(serializers.ModelSerializer):
    project_info = ProjectSerializerShot(source='project')

    class Meta:
        model = RolesInProject
        exclude = ['user', 'project']
        # fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = NVSkill
        fields = '__all__'


class UserSkillsSerializer(serializers.ModelSerializer):
    skill_info = SkillSerializer(source='skill')

    class Meta:
        model = UserSkills
        exclude = ['user']
