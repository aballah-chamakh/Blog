from django.urls import path
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,
                    PostListApiView,PostDetailApiView,post_detail_view)
from django.views.generic import TemplateView
urlpatterns = [
    #path('home/',PostListView.as_view()),
    # path('post/<int:pk>/create-comment/',create_comment),
    path('',TemplateView.as_view(template_name='posts1/post_list.html')),
    path('post/<slug:slug>/',post_detail_view),
    path('post/create/',PostCreateView.as_view()),
    # path('post/<int:pk>/',PostDetailView.as_view()),
    path('post/<int:pk>/update/',PostUpdateView.as_view()),
    path('api/posts/',PostListApiView.as_view()),
    path('api/post/<slug:slug>/',PostDetailApiView.as_view()),


]
