"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os

from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import authentication, permissions

from days_project.core.views import CountryDetailView, CountryListView
from days_project.stay.views import StayListView, StayManagerView
from days_project.user.views import UserListView, UserManagerView

...

schema_view = get_schema_view(
    openapi.Info(
        title="Days API",
        default_version="v1",
        description="Days is a API for counting days",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    url=os.environ.get("SWAGGER_HOST_URL", None),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
    authentication_classes=(authentication.TokenAuthentication,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    # API path
    path("api/v1/user", UserListView.as_view()),
    path("api/v1/user/<str:uuid>", UserManagerView.as_view()),
    path("api/v1/stay", StayListView.as_view()),
    path("api/v1/stay", StayManagerView.as_view()),
    # core dicts
    path("api/v1/country", CountryListView.as_view()),
    path("api/v1/country/<str:code>", CountryDetailView.as_view()),
    # docs
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
