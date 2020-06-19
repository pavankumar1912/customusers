from  rest_framework import serializers
from .models import CustomUser


class Users_serializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
class Register_User_serializera(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

# class User_login(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ['user_id', 'password']
