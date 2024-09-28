from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import BaseSerializer

from days_project.stay.models import StayModel
from days_project.stay.serializer import StaySerializer


class StayListView(generics.ListCreateAPIView):
    serializer_class = StaySerializer
    lookup_field = "uuid"
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: BaseSerializer) -> None:
        serializer.save(user=self.request.user)

    def get_queryset(self) -> QuerySet:
        return StayModel.objects.filter(user_id=self.request.user.id)


class StayManagerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StayModel.objects.all()
    serializer_class = StaySerializer
    http_method_names = ["get", "patch", "delete"]
    lookup_field = "uuid"
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
