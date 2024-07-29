# myApp/models.py

from django.db import models
from django.contrib.auth.models import User

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserSportPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.sport.name}"
