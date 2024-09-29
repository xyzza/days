from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from days_project.core.constants import COUNTRY_CHOICES, COUNTRY_CHOICES_DICT


class CountryListView(APIView):
    def get(self, request: Request) -> Response:
        return Response(data={"country_codes": COUNTRY_CHOICES})


class CountryDetailView(APIView):
    def get(self, request: Request, code: str) -> Response:
        country_name: str | None = COUNTRY_CHOICES_DICT.get(code.upper())
        if country_name is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data={"country_name": country_name})
