from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView

urlpatterns = [
    path('home/',PostListView.as_view()),
    # path('post/<int:pk>/create-comment/',create_comment),
    path('post/create/',PostCreateView.as_view()),
    path('post/<int:pk>/',PostDetailView.as_view()),
    path('post/<int:pk>/update/',PostUpdateView.as_view())

]
