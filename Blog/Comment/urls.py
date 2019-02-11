from django.urls import path,include
from rest_framework import routers
from .views import CommentViewSet,CommentResponseViewSet

router = routers.DefaultRouter()
router.register('comment',CommentViewSet) 
router.register('comment_response',CommentResponseViewSet)

urlpatterns = router.urls
