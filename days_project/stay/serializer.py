from rest_framework import serializers

from days_project.stay.models import StayModel


class StaySerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="email")  # type: ignore

    class Meta:
        model = StayModel
        fields = ["uuid", "entrance_date", "exit_date", "country", "user"]
