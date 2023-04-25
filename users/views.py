from rest_framework.generics import get_object_or_404
# from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView
#     )
# from users.serializers import CustomTokenObtainPairSerializer, UserSerializer,UserProfileSerializer
from users.models import User
from users.serializers import UserSerializer



class SignupView(APIView):
  def post(self, request):
    print(request.data)
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
    else:
      return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
    
    