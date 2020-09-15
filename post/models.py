from django.urls import reverse

from django.db import models
from user.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.TextField()
    total_post = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    description = models.TextField(max_length=800)
    vote = models.IntegerField(default=0, blank=True)
    img_main = models.ImageField(upload_to='post_picture', height_field=None, width_field=None, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = RichTextField(null=True, blank=True, default="Body post")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.datetime.now())
    content = models.CharField(max_length=2000)
    vote = models.IntegerField(default=0)
    reply_comment = models.ForeignKey("self", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.content


