from rest_framework.generics import get_object_or_404
# from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView
    )
from users.models import User
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer,UserProfileSerializer

#회원가입 View
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

#로그인 View 
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class UserView(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response({"message":"수정완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        user = get_object_or_404(User, id=id)
        if request.user == user.user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
          return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)
