from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
  def update(self, validated_data):
    user = super().create(validated_data)
    password = user.password
    user.set_password(password)
    user.save()
    return user
  