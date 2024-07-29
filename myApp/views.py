# myApp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Sport, UserSportPreference

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')  # Preusmjeravanje na glavnu stranicu
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')  # Preusmjeravanje na glavnu stranicu
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Main view
@login_required
def main_view(request):
    user_sports = UserSportPreference.objects.filter(user=request.user)
    return render(request, 'main.html', {'user_sports': user_sports})

# Home view (Početna stranica)
def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')
