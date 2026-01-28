from rest_framework import serializers
from .models import Account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
