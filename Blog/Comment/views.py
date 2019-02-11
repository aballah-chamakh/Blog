from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment,CommentResponse
from .serializers import CommentSerializer,CommentResponseSerializer
from rest_framework.decorators import action

class CommentViewSet(viewsets.ModelViewSet) :
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentResponseViewSet(viewsets.ModelViewSet):
    queryset = CommentResponse.objects.all()
    serializer_class = CommentResponseSerializer
