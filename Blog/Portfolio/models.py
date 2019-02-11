from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    breif = models.TextField()
    image = models.ImageField()
    description = RichTextUploadingField(blank=True, null=True)
    def __str__(self):
        return  'portfolio : '+self.title
