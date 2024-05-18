from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = models.CharField(max_length=32, null=True)
    id = models.IntegerField(null=True, default=1)
    email = models.EmailField(_("email address"), unique=True, primary_key=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

