from django.shortcuts import render
from todo.models import TodoArticle
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from todo.serializers import TodoSerializer, TodoCreateSerializer,TodoListSerializer
import datetime 
from django.views.defaults import permission_denied
from django.http import Http404


class TodoListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        articles = TodoArticle.objects.all()
        serializer = TodoListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # if not request.user.is_authenticated:
        #     return Response({"message":"로그인 해주세요"}, 400)
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class TodoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, id):
        article = get_object_or_404(TodoArticle, id=id)
        serializer = TodoSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        article = get_object_or_404(TodoArticle, id=id)
        if request.user == article.user:
            serializer = TodoCreateSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)
    def delete(self, request, id):
        article = get_object_or_404(TodoArticle, id=id, user=request.user.id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TodoCompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, id):
        article = get_object_or_404(TodoArticle, id=id)
        if request.user == article.user:
            serializer = TodoSerializer(article, data=request.data)
            if serializer.is_valid():
                if request.data.get('is_complete') == "True":
                    serializer.save(completion_at = datetime.datetime.now())        
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


