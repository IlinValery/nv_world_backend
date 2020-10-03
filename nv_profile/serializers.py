from abc import ABC

from rest_framework import serializers


class TokenSerializer(serializers.Serializer, ABC):
    token = serializers.CharField(max_length=255)
