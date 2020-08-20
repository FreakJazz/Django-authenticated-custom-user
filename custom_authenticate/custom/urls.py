from django.urls import path
from .views import *

urlpatterns = [
    path('api/users', UserList.as_view(), name = 'users_list'),
    #path('api/create_users', UserCreate.as_view(), name = 'user_create'),
]