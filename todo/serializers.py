from rest_framework import serializers
from todo.models import TodoArticle


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    #obj 인스턴스의 user속성에서 email값 추출하여 반환해서 user필드에 추가
    def get_user(self,obj):
        return obj.user.email
    class Meta:
        model = TodoArticle
        fields = '__all__'

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoArticle
        fields = ("title", )

class TodoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = TodoArticle
        fields = ('pk', 'title', 'user', 'is_complete', 'created_at','updated_at', 'completion_at')
