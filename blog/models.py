from distutils.command.upload import upload
from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
# Create your models here.


#Categories model
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src ="/media/{}" style="width:250px;height:150px;"  />'.format(self.image))

    def __str__(self):
        return self.title


# Post Model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')

    def image_tag(self):
        return format_html('<img src ="/media/{}" style="width:250px;height:150px;"  />'.format(self.image))

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=280)

