from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class profileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'gender',
            'phone',
            'birthday',
            'isActive',
            'identification',
            'score',
            'workArea',
        )