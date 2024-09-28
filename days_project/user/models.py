from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from days_project.core.models import BaseProjectModel


class CustomUserModelManager(BaseUserManager):
    def create_user(self, email: str, password: str) -> "CustomUserModel":
        email = self.normalize_email(email)
        user: "CustomUserModel" = self.model(email=email)  # type: ignore

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str) -> "CustomUserModel":
        user: "CustomUserModel" = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class CustomUserModel(AbstractBaseUser, BaseProjectModel, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    is_staff = models.BooleanField(null=False, default=False, blank=True)

    objects = CustomUserModelManager()

    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.email
