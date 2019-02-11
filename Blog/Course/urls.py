
from django.urls import path
from .views import CourseListView,CourseDetailView,ProjectListView,ProjectDetailView

urlpatterns = [

    path('courses/',CourseListView.as_view()),
    path('courses/<int:pk>/',CourseDetailView.as_view()),
    path('projects/',ProjectListView.as_view()),
    path('project/<int:pk>/',ProjectDetailView.as_view()),

]
