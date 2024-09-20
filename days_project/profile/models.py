from django.db import models

from days_project.core.models import BaseProjectModel


class ProfileModel(BaseProjectModel):
    email = models.EmailField(max_length=250, null=False, blank=False, unique=True)
