from django.db import models

from days_project.core.constants import COUNTRY_CHOICES
from days_project.core.models import BaseProjectModel
from days_project.user.models import CustomUserModel


class StayModel(BaseProjectModel):
    user = models.ForeignKey(CustomUserModel, on_delete=models.PROTECT)
    entrance_date = models.DateTimeField()
    exit_date = models.DateTimeField()
    country = models.CharField(max_length=200, choices=COUNTRY_CHOICES, null=False, blank=False)
