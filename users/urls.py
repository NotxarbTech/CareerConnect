from django.urls import path
from . import views

# Registers the app name
app_name = 'users'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('signup', views.SignupView, name='signup'),
    path('', views.index, name='index'),
]