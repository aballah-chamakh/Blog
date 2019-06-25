from rest_framework import serializers
from .models import Post
from Course.serializers import CourseDetailSerializer,ProjectDetailSerializer
class PostListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Post
        fields = ('id','slug','title','image','description','order')

class PostDetailSerializer(serializers.ModelSerializer):
    course_or_project = serializers.SerializerMethodField()
    class Meta :
        model = Post
        fields = ('id','slug','title','image','description','order','course_or_project')
    def get_course_or_project(self,post_obj):
        if post_obj.course :
            course_obj = post_obj.course
            serializer = CourseDetailSerializer(course_obj,many=False,context={'request':self.context['request']})
            return {'type':'course','serie':serializer.data}
        elif post_obj.project :
            project_obj = post_obj.project
            serializer = ProjectDetailSerializer(project_obj,many=False,context={'request':self.context['request']})
            return {'type':'project','serie':serializer.data}
        else :
            return None
