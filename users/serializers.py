from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    def create(self, validated_data):
        print(validated_data)
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    def update(self, instance, validated_data):
        user = super().create(instance, validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


#로그인
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token