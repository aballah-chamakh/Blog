from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Course,Project


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
