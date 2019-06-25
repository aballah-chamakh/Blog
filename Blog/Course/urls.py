
from django.urls import path
from .views import (CourseListView,CourseDetailView,ProjectListView,ProjectDetailView
                    ,CourseListApiView,CourseDetailApiView,ProjectListApiView,ProjectDetailApiView
                    ,project_detail_view,course_detail_view)

from django.views.generic import TemplateView

urlpatterns = [
    path('courses/',TemplateView.as_view(template_name='courses1/course_list.html')),
    path('courses/<slug:slug>/',course_detail_view),
    path('projects/',TemplateView.as_view(template_name='projects1/project_list.html')),
    path('project/<slug:slug>/',project_detail_view),
    # path('courses/',CourseListView.as_view()),
    # path('courses/<int:pk>/',CourseDetailView.as_view()),
    # path('projects/',ProjectListView.as_view()),
    # path('project/<int:pk>/',ProjectDetailView.as_view()),
    # api
    path('api/courses/',CourseListApiView.as_view()),
    path('api/course/<slug:slug>/',CourseDetailApiView.as_view()),
    path('api/projects/',ProjectListApiView.as_view()),
    path('api/project/<slug:slug>/',ProjectDetailApiView.as_view()),
]
