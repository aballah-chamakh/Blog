from rest_framework import serializers
from .models import Course,Project
from Post.models import Post

class ListPostSerializer(serializers.ModelSerializer):
    class Meta :
        model = Post
        fields = ('id','slug','title','image','order')

class CourseListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Course
        fields = ('id','slug','title','image','description')

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Project
        fields = ('id','slug','title','image','description')

class CourseDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    class Meta :
        model = Course
        fields = ('id','slug','title','image','description','posts')
    def get_posts(self,course_obj):
        posts_qs = course_obj.post_set.all()
        serializer = ListPostSerializer(posts_qs,many=True)
        return serializer.data

class ProjectDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    class Meta :
        model = Project
        fields = ('id','slug','title','image','description','posts')
    def get_posts(self,course_obj):
        posts_qs = course_obj.post_set.all()
        serializer = ListPostSerializer(posts_qs,many=True)
        return serializer.data
