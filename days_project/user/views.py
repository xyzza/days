from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser

from days_project.user.models import CustomUserModel
from days_project.user.serializer import CustomUserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = CustomUserModel.objects.filter(is_staff=False)
    serializer_class = CustomUserSerializer
    lookup_field = "uuid"
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]


class UserManagerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "delete", "patch"]
    lookup_field = "uuid"
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
