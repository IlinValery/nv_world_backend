from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from nv_service.serializers import StatusSerializer


class TestConnection(APIView):
    def get(self, request, format=None):
        print(request)
        serializer = StatusSerializer(data={
            "status": True
        })
        serializer.is_valid()
        return Response(serializer.data)
