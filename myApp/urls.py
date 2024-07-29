from django.urls import path
from .views import signup_view, login_view, main_view, home_view, about_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('main/', main_view, name='main'),  # Glavna stranica
    path('', home_view, name='home'),  # Početna stranica
    path('about/', about_view, name='about'),  # Dodajemo URL za about stranicu

]
