from rest_framework import serializers
from django.contrib.auth.models import User
#from accounts.models import User
from django.contrib.auth.models import AbstractUser, UserManager

class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer

    Handles the serialisation of the 'User' model

    The fields to be serialized are:
    -   username
    -   password
    """

    class Meta:
        model = User
        fields = ('username', 'password')

