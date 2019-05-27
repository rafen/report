from rest_framework import serializers

from ..models import User


class UserLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['language']
