from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Course,Project
from rest_framework import generics,mixins
from .serializers import (CourseListSerializer,CourseDetailSerializer,
                         ProjectDetailSerializer,ProjectListSerializer)




# def course_list_view(request):
#     courses_objects = Course.objects.all()
#     context = {
#     'courses_objects':courses_objects
#     }
#     return render(request,'courses/course_list.html',context)

def course_detail_view(request,slug):
    coure_obj = Course.objects.get(slug=slug)
    context = {'course_obj' : course_obj}
    return render(request,'courses1/course_detail.html',context)

# def project_list_view(request):
#     projects_objects = Project.objects.all()
#     context = {
#     'projects_objects':projects_objects
#     }
#     return render(request,'projects/project_list.html',context)

def project_detail_view(request,slug):
    project_obj = Project.objects.get(slug=slug)
    context = {'project_obj' : project_obj}
    return render(request,'projects1/project_detail.html',context)

class CourseListView(ListView):
    queryset = Course.objects.all()
    template_name = 'courses/course_list.html'


class CourseDetailView(DetailView):
    queryset = Course.objects.all()
    template_name = 'courses/course_detail.html'
    model = Course
    def get_context_data(self, **kwargs):

        context = {}
        if self.object:
            context['object'] = self.object
            first_post_id = self.object.post_set.all()[0].id
            context['first_post_id'] = first_post_id
        return context


class ProjectListView(ListView):
    queryset = Project.objects.all()
    template_name = 'projects/projects_list.html'


class ProjectDetailView(DetailView):
    queryset = Project.objects.all()
    template_name = 'projects/project_detail.html'
    model = Project
    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['object'] = self.object
            if self.object.post_set.count() > 0 :
                first_post_id = self.object.post_set.all()[0].id
                context['first_post_id'] = first_post_id
        return context

class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'slug'

class ProjectListApiView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer

class ProjectDetailApiView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'slug'
