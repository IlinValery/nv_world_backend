from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate, login
from rest_framework import status
from nv_profile.serializers import TokenSerializer
from nv_profile.models import NVUserProfile
from nv_projects.models import NVProject
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


        if username and password:
            is_exist = len(NVUserProfile.objects.filter(username=username))
            if is_exist:
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
                user = NVUserProfile.objects.create_user(username=username, password=password, name=realname)
                # TODO choose project here automatically for fresh user

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
