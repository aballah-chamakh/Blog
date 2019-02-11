from django.db import models
from Post.models import  Post
from Course.models import Course,Project
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Comment(models.Model):
    owner     = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    content =  models.TextField()
    likes   = models.ManyToManyField(User,blank=True,related_name='comment_likes')

    def __str__(self):
        return self.owner.username

class CommentResponse(models.Model):
    owner     = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    content =  models.TextField(null=True,blank=True)
    likes   = models.ManyToManyField(User,blank=True,related_name='res_comment_likes')
    
    def __str__(self):
        return self.owner.username
