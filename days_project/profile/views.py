from rest_framework import generics

from days_project.profile.models import ProfileModel
from days_project.profile.serializer import ProfileSerializer


class ProfileListView(generics.ListCreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "uuid"


class ProfileManagerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ["get", "patch", "delete"]
    lookup_field = "uuid"
