from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'gender',   
            'phone',
            'birthday',
            'isActive',
            'identification',
            'score',
            'workArea',
        )