from django.urls import path
from .views import *

urlpatterns = [
    path('api/profiles', profilesList.as_view(), name = 'profiles_list'),
    #path('api/create_users', UserCreate.as_view(), name = 'user_create'),
]