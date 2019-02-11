from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from Course.models import Course,Project
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

def get_post_order(self):
    if len(Post.objects.all()) == 0 :
        return 1
    obj = Post.objects.lastest('id')
    return obj.order + 1

# Create your models here.
class Post(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,blank=True,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField()
    title = models.CharField(max_length=255)
    slug  = models.SlugField(blank=True,null=True)
    description = RichTextUploadingField(blank=True, null=True)
    published = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    technology = models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):
        return self.title+' order : '+str(self.order)
    class Meta :
        ordering = ['-id']




@receiver(post_save, sender=Post)
def create_user_profile(sender, instance, created, **kwargs):
    if created :
        qs = None
        if instance.project :
            qs = Post.objects.all().filter(project = project)

        elif instance.course :
            qs = Post.objects.all().filter(project = project)
        if qs :
            instance.order = len(qs) + 1
