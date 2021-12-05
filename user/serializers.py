from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User

from funding.models import Funding


class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']




class listserializer(serializers.ModelSerializer):
    class Meta:
        model=Funding
        fields='__all__'
