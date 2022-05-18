from django.contrib.auth.models import User
from django.db import models


class Analysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default="")
    irony = models.CharField(max_length=30, default="")
    score_tag = models.CharField(max_length=30, default="")
    confidence = models.IntegerField(default=0)
