from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    about = models.TextField()
    member_since = models.DateField(default=timezone.now)
    nfc_id = models.IntegerField()
