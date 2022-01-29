from datetime import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    thumbnail=models.ImageField(upload_to='media/blogs-thumbnail/%Y/%m/%d/')
    title=models.CharField(max_length=100)
    mins_required=models.IntegerField()
    blog_desc=RichTextUploadingField()
    created_date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title