import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        db_table = "users"


class Team(models.Model):
    class Meta:
        db_table = "teams"
