from rest_framework import serializers
from .models import UserDetail, Credential

class UserDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('id', 'name', 'image', 'college', 'roll')

class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credential
        fields = ('username', 'password')
