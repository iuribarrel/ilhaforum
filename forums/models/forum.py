from django.db import models
from django.contrib.auth.models import User
from .base_model import BaseModel


class Forum(BaseModel):
    description = models.CharField(max_length=200)