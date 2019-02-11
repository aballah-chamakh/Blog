from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
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
