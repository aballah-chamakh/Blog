from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from Post.utils import unique_slug_generator
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        posts = self.post_set.all()
        course_posts = ''
        if posts :
            for post in posts :
                course_posts += post.title+' , '
        return self.title+' ==> ( '+course_posts+' )'
    def get_all_posts(self):
        posts = self.post_set.all()
        return posts


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        posts = self.post_set.all()
        project_posts = ''
        if posts :
            for post in posts :
                project_posts += post.title+' , '

        return self.title+' ==> ( '+project_posts+' )'

    def get_all_posts(self):
        posts = self.post_set.all()
        return posts

@receiver(post_save, sender=Course)
def set_course_slug(sender, instance, created, **kwargs):
    if created :
        instance.slug = unique_slug_generator(instance)

@receiver(post_save, sender=Project)
def set_project_slug(sender, instance, created, **kwargs):
    if created :
        instance.slug = unique_slug_generator(instance)
