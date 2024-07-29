from django.db import models
from django.contrib.auth.models import User

class Sport(models.Model):
    naziv_sporta = models.CharField(max_length=100)
    description = models.TextField()

class UserSportPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Sport, UserSportPreference

# Main view
@login_required
def main_view(request):
    user_sports = UserSportPreference.objects.filter(user=request.user)
    return render(request, 'main.html', {'user_sports': user_sports})
