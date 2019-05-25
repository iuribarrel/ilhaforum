from django.db import models
from .base_model import BaseModel


class Topic(BaseModel):
    name = models.CharField(max_length=200)
    forum = models.ForeignKey('Forum', on_delete=models.CASCADE)