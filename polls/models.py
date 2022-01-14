from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.first_name


class Link(models.Model):
    full = models.URLField(max_length=256)
    short = models.URLField(max_length=256, primary_key=True)

    def __str__(self):
        return self.short
