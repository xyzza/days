import uuid

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from days_project.user.models import CustomUserModel


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
    )

    class Meta:
        model = CustomUserModel
        fields = ["uuid", "email", "password"]

    def create(self, validated_data: dict) -> CustomUserModel:
        validated_data["password"] = make_password(
            validated_data.get("password", str(uuid.uuid4()))
        )
        return super(CustomUserSerializer, self).create(validated_data)
