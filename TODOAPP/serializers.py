from rest_framework import serializers
from rest_framework.authtoken.admin import *


from .models import Todo,User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields='__all__'

class userSerializers(serializers.ModelSerializer):
    # user = serializers.Field(source='user.username')

    # def get_user(self, obj):
    #     return obj.user.username
    class Meta:
        model=User
        fields=['username','password']


    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



