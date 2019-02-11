from rest_framework import serializers
from .models import Comment,CommentResponse
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['id','username']


class CommentResponseSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField('grab_all_likes')
    class Meta :
        model = Comment
        fields = ['content','likes']
    def grab_all_likes(self,obj):
        user_likes = obj.likes.all()
        serializer = UserSerializer(user_likes,many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    comment_responses = serializers.SerializerMethodField(method_name='grab_comment_responses',read_only=True)
    object_title = serializers.CharField(source='content_object.title',read_only=True)
    class Meta :
        model = Comment
        fields = ['id','content','object_title','comment_responses']
    def grab_comment_responses(self,obj):
        comment_responses = obj.commentresponse_set.all()
        serializer = CommentResponseSerializer(comment_responses,many=True)
        return serializer.data
