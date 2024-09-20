from rest_framework import serializers

from days_project.profile.models import ProfileModel


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileModel
        exclude = ["id"]
