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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Post_as_author")
    date = models.DateField(default=timezone.now)
    description = models.TextField(max_length=800)
    img_main = models.ImageField(upload_to='post_picture', height_field=None, width_field=None, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = RichTextField(null=True, blank=True, default="Body post")
    users_like = models.ManyToManyField(User)

    def total_likes(self):
        return self.users_like.count()

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse('home')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Comment_as_author")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.datetime.now())
    content = models.CharField(max_length=2000)
    # reply_comment = models.ForeignKey("self", on_delete=models.CASCADE, blank=True)
    users_comment = models.ManyToManyField(User)

    def __str__(self):
        return self.content
