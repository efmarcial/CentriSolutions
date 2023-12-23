from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class CustomUser(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Service(models.Model):
    service_name = models.CharField(max_length=100)

    def __str__(self):
        return self.service_name


class Page(models.Model):
    page_title = models.CharField(max_length=100)
    service_page = models.BooleanField(default=False)

    def __str__(self):
        return self.page_title



