from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    owner = models.ForeignKey(User, models.CASCADE)
    text = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
