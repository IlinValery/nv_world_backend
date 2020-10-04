from django.db.models import QuerySet
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate, login
from rest_framework import status
from nv_profile.serializers import TokenSerializer, UserSerializer, UserRolesInTeamSerializer, UserSkillsSerializer, \
    RoomSerializer, SkillSerializer
from nv_profile.models import NVUserProfile, UserSkills, NVRoom, NVSkill
from nv_projects.models import NVProject, RolesInProject
import random
from datetime import datetime, timedelta

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def jwt_response_payload_handler(user):
    data_to_jwt = {
        'user_id': user.id,
        'username': user.username
    }
    if user.name:
        data_to_jwt['name'] = user.name
    else:
        data_to_jwt['name'] = ""
    if user.email:
        data_to_jwt['email'] = user.email
    else:
        data_to_jwt['email'] = ""
    return data_to_jwt


class LoginView(APIView):
    """
    POST api/auth/login/
    --data:
            {
              "username":"qwe",
              "realname": "Test test",
              "password": "qazswxde"
            }
    RESPONSE: token in JWT format
    """
    permission_classes = (permissions.AllowAny,)
    queryset = NVUserProfile.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        realname = request.data.get("realname", "")
        password = request.data.get("password", "")
        is_male = request.data.get("is_male", "")
        print(username, realname, password, is_male)
        if username and password:
            is_exist = len(NVUserProfile.objects.filter(username=username))
            if not is_exist:
                user = NVUserProfile.objects.create_user(username=username, password=password, name=realname,
                                                         is_male=is_male)
                project = NVProject.objects.order_by('?').first()
                roles = RolesInProject.RolesInProjectNames.choices
                role = roles[random.randint(0, len(roles) - 1)][0]
                membership = RolesInProject.objects.create(user=user, project=project, role=role)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')

                serializer = TokenSerializer(data={
                    # using drf jwt utility functions to generate a token
                    "token": jwt_encode_handler(
                        jwt_response_payload_handler(user)
                    )})
                serializer.is_valid()
                return Response(serializer.data)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class LogoutView(APIView):
    """
    GET /api/auth/logout/
    RESPONSE: OK
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        request.session.delete()
        return Response(status=status.HTTP_200_OK)


class UserView(APIView, PageNumberPagination):
    """
    GET /api/user/:number
    RESPONSE:
        {

        }    """

    def get(self, request, user_id):
        user = NVUserProfile.objects.get(id=user_id)
        user_roles = RolesInProject.objects.filter(user=user)
        if user.current_room is None:
            if len(user_roles):
                user.current_room = user_roles[0].project.room
            else:
                rooms = NVRoom.objects.order_by('?')
                if rooms.count() > 0:
                    user.current_room = rooms[0]
            user.save()

        user_skills = UserSkills.objects.filter(user=user)
        if user:
            serializer_user = UserSerializer(instance=user)
            serializer_roles = UserRolesInTeamSerializer(instance=user_roles, many=True)

            serializer_skills = UserSkillsSerializer(instance=user_skills, many=True)

            return Response({"user_info": serializer_user.data,
                             "roles": serializer_roles.data if len(user_roles) else [],
                             "skills": serializer_skills.data if len(user_skills) else []
                             })
        else:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)


class CurrentRoomView(APIView):
    """
    Get people in Room
    """

    def get(self, request, user_id):
        user = NVUserProfile.objects.get(id=user_id)
        room = user.current_room
        cur_time = datetime.now()
        delta = timedelta(seconds=10)
        users_in_room = NVUserProfile.objects.filter(current_room=room, last_active_room__minute=cur_time.minute)
        print(users_in_room)
        user.last_active_room = datetime.now()
        user.save()

        data = {"room_info": RoomSerializer(instance=room).data}
        if users_in_room.count() > 0:
            data["users"] = UserSerializer(instance=users_in_room, many=True).data
        return Response(data)


class SkillsView(APIView):

    def get(self, request):
        skills_unique = UserSkills.objects.all().distinct('skill')
        skills = []
        for skill_info in skills_unique:
            skills.append(skill_info.skill)
        return Response({"skills": SkillSerializer(skills, many=True).data})
